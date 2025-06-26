from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import json
import os

def application(environ, start_response):
    """The main WSGI application that handles all requests"""
    
    # Get the request method and path
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    
    # Route the request based on the path
    if path == '/' or path == '/home':
        response = handle_home(environ)
    elif path == '/about':
        response = handle_about(environ)
    elif path == '/contact':
        response = handle_contact(environ)
    elif path.startswith('/static/'):
        response = handle_static(environ)
    elif path.startswith('/api/'):
        response = handle_api(environ)
    else:
        response = handle_not_found(environ)
    
    # Start the response with the appropriate status and headers
    start_response(response['status'], response['headers'])
    
    # Return the response body as a list of bytes (WSGI requirement)
    return [response['body'].encode('utf-8')]

def handle_home(environ):
    """Handle requests to the home page"""
    return {
        'status': '200 OK',
        'headers': [('Content-type', 'text/html; charset=utf-8')],
        'body': f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Nilay Biswas - Cloud Engineer</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body>
                <nav>
                    <a href="/home">Home</a>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                    <a href="/static/sample.pdf">Sample PDF</a>
                </nav>
                <h1>Welcome to Nilay Biswas's Portfolio</h1>
                <p>Cloud Engineer at Quantzent Pvt Ltd</p>
                <img src="/static/logo.png" alt="Logo" width="200">
                <div class="social-links">
                    <p><strong>GitHub:</strong> <a href="https://github.com/nilaycodetodecode/nilaypythonwebsite.git" target="_blank">nilaycodetodecode</a></p>
                    <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/nilay-biswas-7aba07316" target="_blank">Nilay Biswas</a></p>
                </div>
                <footer>
                    <p>Powered by Python WSGI | Static IP: 18.168.21.214</p>
                </footer>
            </body>
            </html>
        """
    }

def handle_about(environ):
    """Handle requests to the about page"""
    return {
        'status': '200 OK',
        'headers': [('Content-type', 'text/html; charset=utf-8')],
        'body': """
            <!DOCTYPE html>
            <html>
            <head>
                <title>About Nilay Biswas</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body>
                <nav>
                    <a href="/home">Home</a>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                </nav>
                <h1>About Nilay Biswas</h1>
                <p>Cloud Engineer at Quantzent Pvt Ltd with expertise in Python, AWS, and web technologies.</p>
                <p>This website serves as a portfolio and demonstration of Python WSGI capabilities.</p>
                <h2>Technical Skills</h2>
                <ul>
                    <li>Cloud Computing (AWS, GCP)</li>
                    <li>Python Development</li>
                    <li>Web Services</li>
                    <li>Data Science</li>
                </ul>
                <footer>
                    <p>Powered by Python WSGI | Static IP: 18.168.21.214</p>
                </footer>
            </body>
            </html>
        """
    }

def handle_contact(environ):
    """Handle requests to the contact page"""
    return {
        'status': '200 OK',
        'headers': [('Content-type', 'text/html; charset=utf-8')],
        'body': f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Contact Nilay Biswas</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body>
                <nav>
                    <a href="/home">Home</a>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                </nav>
                <h1>Contact Information</h1>
                <div class="contact-info">
                    <p><strong>Name:</strong> Nilay Biswas</p>
                    <p><strong>Email:</strong> <a href="mailto:nilaybiswas.datascience.2021@gmail.com">nilaybiswas.datascience.2021@gmail.com</a></p>
                    <p><strong>Phone:</strong> +91 8391859206</p>
                    <p><strong>Company:</strong> Quantzent Pvt Ltd</p>
                    <p><strong>Position:</strong> Cloud Engineer</p>
                </div>
                <div class="social-links">
                    <p><strong>GitHub:</strong> <a href="https://github.com/nilaycodetodecode/nilaypythonwebsite.git" target="_blank">nilaycodetodecode</a></p>
                    <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/nilay-biswas-7aba07316" target="_blank">Nilay Biswas</a></p>
                </div>
                <footer>
                    <p>Powered by Python WSGI | Static IP: 18.168.21.214</p>
                </footer>
            </body>
            </html>
        """
    }

def handle_static(environ):
    """Handle static file requests"""
    path = environ['PATH_INFO']
    file_path = path[1:]  # Remove the leading slash
    
    # Create static directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
    # Sample static files (in a real app, these would be actual files)
    static_files = {
        'style.css': """
            body { 
                font-family: Arial, sans-serif; 
                line-height: 1.6; 
                max-width: 800px; 
                margin: 0 auto; 
                padding: 20px; 
            }
            nav { 
                background: #f4f4f4; 
                padding: 10px; 
                margin-bottom: 20px; 
            }
            nav a { 
                margin-right: 15px; 
                text-decoration: none; 
            }
            footer { 
                margin-top: 20px; 
                border-top: 1px solid #ccc; 
                padding-top: 10px; 
                font-size: 0.9em;
            }
            img {
                max-width: 100%;
                height: auto;
            }
            .contact-info, .social-links {
                background: #f9f9f9;
                padding: 15px;
                border-radius: 5px;
                margin: 15px 0;
            }
            ul {
                padding-left: 20px;
            }
        """,
        'logo.png': """
            [This would be binary PNG data in a real implementation]
            For demo purposes, we're just returning a placeholder
        """,
        'sample.pdf': """
            [This would be binary PDF data in a real implementation]
            For demo purposes, we're just returning a placeholder
        """
    }
    
    # Check if file exists in our static files
    filename = os.path.basename(file_path)
    if filename in static_files:
        content = static_files[filename]
        
        # Determine content type based on file extension
        if filename.endswith('.css'):
            content_type = 'text/css'
        elif filename.endswith('.png'):
            content_type = 'image/png'
        elif filename.endswith('.pdf'):
            content_type = 'application/pdf'
        else:
            content_type = 'text/plain'
            
        return {
            'status': '200 OK',
            'headers': [('Content-type', content_type)],
            'body': content
        }
    else:
        return handle_not_found(environ)

def handle_api(environ):
    """Handle API requests"""
    path = environ['PATH_INFO']
    
    if path == '/api/info':
        return {
            'status': '200 OK',
            'headers': [('Content-type', 'application/json')],
            'body': json.dumps({
                'server': 'Nilay Biswas Portfolio',
                'ip': '18.168.21.214',
                'port': 8000,
                'status': 'online',
                'owner': {
                    'name': 'Nilay Biswas',
                    'email': 'nilaybiswas.datascience.2021@gmail.com',
                    'company': 'Quantzent Pvt Ltd',
                    'position': 'Cloud Engineer'
                }
            })
        }
    else:
        return handle_not_found(environ)

def handle_not_found(environ):
    """Handle 404 Not Found errors"""
    return {
        'status': '404 Not Found',
        'headers': [('Content-type', 'text/html; charset=utf-8')],
        'body': """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Page Not Found</title>
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body>
                <nav>
                    <a href="/home">Home</a>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                </nav>
                <h1>404 - Page Not Found</h1>
                <p>The requested URL was not found on this server.</p>
                <p><a href="/home">Return to the home page</a></p>
                <footer>
                    <p>Powered by Python WSGI | Static IP: 18.168.21.214</p>
                </footer>
            </body>
            </html>
        """
    }

if __name__ == '__main__':
    # Create the WSGI server
    port = 8000
    static_ip = '18.168.21.214'  # Updated static IP
    
    print(f"Serving Nilay Biswas's portfolio at http://{static_ip}:{port}")
    print("Available routes:")
    print(f"  http://{static_ip}:{port}/home")
    print(f"  http://{static_ip}:{port}/about")
    print(f"  http://{static_ip}:{port}/contact")
    print(f"  http://{static_ip}:{port}/static/style.css")
    print(f"  http://{static_ip}:{port}/api/info")
    
    with make_server('', port, application) as httpd:
        # Serve until process is killed
        httpd.serve_forever()