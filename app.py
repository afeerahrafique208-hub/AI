from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

HUMANIZE_PROMPT = """You are an advanced AI content humanizer and editor. Your task is to rewrite the provided text so that it reads naturally and professionally, as if a skilled human writer created it. Follow these instructions carefully:

1. Maintain the original meaning and key facts, numbers, or terms.
2. Rewrite sentences in your own words—avoid copying phrases verbatim.
3. Use a clear, engaging, and conversational tone suitable for publication.
4. Vary sentence length and structure to improve readability and flow.
5. Prefer active voice over passive voice wherever possible.
6. Add subtle stylistic enhancements: transitions, headings, bullet points, or lists if they improve clarity.
7. Keep paragraphs concise and well-structured.
8. Avoid jargon unless necessary; make complex ideas easy to understand.
9. Ensure grammar, punctuation, and spelling are perfect.
10. The output should be ready to publish as high-quality, human-like content.

Text to humanize: {input_text}"""

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/styles.css')
def serve_css():
    return send_from_directory('.', 'styles.css')

@app.route('/script.js')
def serve_js():
    return send_from_directory('.', 'script.js')

@app.route('/api/humanize', methods=['POST'])
def humanize():
    try:
        data = request.get_json()
        input_text = data.get('text', '').strip()
        
        if not input_text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Use OpenAI API to humanize the text
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return jsonify({
                'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY environment variable.'
            }), 500
        
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert content editor and humanizer. Rewrite text to be natural, engaging, and professional while preserving all key information and meaning."
                    },
                    {
                        "role": "user",
                        "content": HUMANIZE_PROMPT.format(input_text=input_text)
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            humanized_text = response.choices[0].message.content.strip()
            
            return jsonify({
                'humanized_text': humanized_text,
                'original_length': len(input_text),
                'humanized_length': len(humanized_text)
            })
            
        except Exception as e:
            return jsonify({
                'error': f'OpenAI API error: {str(e)}'
            }), 500
            
    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
