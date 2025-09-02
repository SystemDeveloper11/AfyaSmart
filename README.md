<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AfyaSmart Health Assistant - README</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <!-- GitHub Markdown CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css">
    <style>
        :root {
            --primary-color: #4e73df;
            --secondary-color: #1cc88a;
            --accent-color: #ff6b6b;
            --dark-color: #2d3748;
            --light-color: #f8f9fc;
        }
        
        body {
            font-family: 'Open Sans', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
            color: var(--dark-color);
            line-height: 1.6;
        }
        
        .header {
            background: linear-gradient(120deg, var(--primary-color), #6c8ef5);
            color: white;
            padding: 3rem 0;
            margin-bottom: 2rem;
            border-radius: 0 0 20px 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        
        .header h1 {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 2.8rem;
            margin-bottom: 0.5rem;
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
            max-width: 800px;
            margin: 0 auto;
        }
        
        .container-main {
            max-width: 900px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 25px rgba(0, 0, 0, 0.08);
            overflow: hidden;
            margin-bottom: 3rem;
        }
        
        .markdown-body {
            padding: 2.5rem;
            font-family: 'Open Sans', sans-serif;
            font-size: 16px;
        }
        
        .markdown-body h1, 
        .markdown-body h2, 
        .markdown-body h3, 
        .markdown-body h4 {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: var(--primary-color);
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }
        
        .markdown-body h1 {
            font-size: 2em;
            margin-top: 0;
        }
        
        .markdown-body img {
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 1.5rem 0;
            max-width: 100%;
        }
        
        .contact-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 2rem 0;
        }
        
        .contact-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 12px 25px;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .btn-whatsapp {
            background: linear-gradient(120deg, #25D366, #128C7E);
            color: white;
        }
        
        .btn-phone {
            background: linear-gradient(120deg, #007bff, #0056b3);
            color: white;
        }
        
        .btn-email {
            background: linear-gradient(120deg, #ff6b6b, #c53030);
            color: white;
        }
        
        .btn-portfolio {
            background: linear-gradient(120deg, var(--secondary-color), #0fa37c);
            color: white;
        }
        
        .btn-live {
            background: linear-gradient(120deg, #6c8ef5, var(--primary-color));
            color: white;
        }
        
        .contact-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
            color: white;
            text-decoration: none;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin: 2rem 0;
        }
        
        .feature-card {
            background: linear-gradient(135deg, #f8f9fc 0%, #eef2f7 100%);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            border-left: 4px solid var(--primary-color);
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
        }
        
        .feature-card h4 {
            font-family: 'Poppins', sans-serif;
            color: var(--primary-color);
            margin-top: 0;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .footer {
            text-align: center;
            padding: 2rem 0;
            color: #6c757d;
            font-size: 0.9rem;
        }
        
        .tech-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 1.5rem 0;
        }
        
        .tech-badge {
            background: linear-gradient(135deg, #e9ecef 0%, #dee2e6 100%);
            padding: 5px 15px;
            border-radius: 50px;
            font-size: 0.85rem;
            font-weight: 500;
            color: #495057;
        }
        
        .screenshot {
            text-align: center;
            margin: 2rem 0;
        }
        
        .screenshot img {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2.2rem;
            }
            
            .contact-buttons {
                flex-direction: column;
                align-items: center;
            }
            
            .contact-btn {
                width: 80%;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header class="header text-center">
        <div class="container">
            <h1><i class="fas fa-robot me-2"></i> AfyaSmart Health Assistant</h1>
            <p>An intelligent health assistant that provides symptom analysis, health recommendations, and medication guidance</p>
            
            <div class="contact-buttons">
                <a href="https://wa.me/254703917940" class="contact-btn btn-whatsapp" target="_blank">
                    <i class="fab fa-whatsapp"></i> WhatsApp
                </a>
                <a href="tel:+254102273123" class="contact-btn btn-phone">
                    <i class="fas fa-phone"></i> Call Now
                </a>
                <a href="mailto:remotaskfreelancer@gmail.com" class="contact-btn btn-email">
                    <i class="fas fa-envelope"></i> Email
                </a>
                <a href="https://github.com/brianmbakadev" class="contact-btn btn-portfolio" target="_blank">
                    <i class="fas fa-user"></i> Portfolio
                </a>
                <a href="https://afyasmartdoc.com" class="contact-btn btn-live" target="_blank">
                    <i class="fas fa-external-link-alt"></i> Live Demo
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <div class="container container-main">
        <article class="markdown-body">
            <h1>AfyaSmart Health Assistant</h1>
            
            <p>AfyaSmart is an intelligent health assistant designed to provide users with preliminary health assessments based on their symptoms. It offers possible health issues, actionable recommendations, and medication guidance in a user-friendly interface.</p>
            
            <div class="screenshot">
                <img src="https://via.placeholder.com/800x450?text=AfyaSmart+Screenshot" alt="AfyaSmart Health Assistant Interface">
                <p><em>AfyaSmart Health Assistant Interface</em></p>
            </div>
            
            <h2>Features</h2>
            
            <div class="features-grid">
                <div class="feature-card">
                    <h4><i class="fas fa-diagnoses"></i> Symptom Analysis</h4>
                    <p>Input your symptoms and receive a detailed analysis of possible health conditions with explanations.</p>
                </div>
                
                <div class="feature-card">
                    <h4><i class="fas fa-tasks"></i> Actionable Recommendations</h4>
                    <p>Get practical advice on what to do to alleviate symptoms and when to seek professional medical help.</p>
                </div>
                
                <div class="feature-card">
                    <h4><i class="fas fa-capsules"></i> Medication Guidance</h4>
                    <p>Receive information about potential medications, including dosage recommendations and precautions.</p>
                </div>
                
                <div class="feature-card">
                    <h4><i class="fas fa-user-md"></i> Health Professional Connection</h4>
                    <p>Easy access to connect with healthcare professionals for further consultation when needed.</p>
                </div>
            </div>
            
            <h2>Technology Stack</h2>
            
            <div class="tech-badges">
                <span class="tech-badge">HTML5</span>
                <span class="tech-badge">CSS3</span>
                <span class="tech-badge">JavaScript</span>
                <span class="tech-badge">Bootstrap 5</span>
                <span class="tech-badge">Font Awesome</span>
                <span class="tech-badge">Google Fonts</span>
                <span class="tech-badge">GitHub Pages</span>
            </div>
            
            <h2>Installation</h2>
            
            <p>To run AfyaSmart locally, follow these steps:</p>
            
            <ol>
                <li>Clone the repository:
                    <pre><code>git clone https://github.com/brianmbakadev/afyasmart.git</code></pre>
                </li>
                <li>Navigate to the project directory:
                    <pre><code>cd afyasmart</code></pre>
                </li>
                <li>Open <code>index.html</code> in your web browser:
                    <pre><code>open index.html</code></pre>
                </li>
            </ol>
            
            <h2>Usage</h2>
            
            <p>Using AfyaSmart is simple and intuitive:</p>
            
            <ol>
                <li>Open the application in your web browser</li>
                <li>Enter your name for a personalized experience</li>
                <li>Describe your symptoms in the chat interface</li>
                <li>Receive a detailed health assessment with possible conditions</li>
                <li>Follow the recommended actions and medication guidance</li>
                <li>Contact a healthcare professional if symptoms persist or worsen</li>
            </ol>
            
            <h2>Project Structure</h2>
            
            <pre><code>afyasmart/
├── index.html          # Main HTML file
├── style.css           # Additional styles (if needed)
├── script.js           # JavaScript functionality (if needed)
├── assets/             # Directory for images and other assets
│   ├── images/         # Screenshots and logos
│   └── icons/          # Application icons
└── README.md           # Project documentation</code></pre>
            
            <h2>Contributing</h2>
            
            <p>Contributions are welcome! If you'd like to contribute to AfyaSmart, please follow these steps:</p>
            
            <ol>
                <li>Fork the repository</li>
                <li>Create a new branch for your feature or bug fix</li>
                <li>Make your changes and test thoroughly</li>
                <li>Submit a pull request with a detailed description of your changes</li>
            </ol>
            
            <h2>Contact the Developer</h2>
            
            <p>AfyaSmart was developed by <strong>Brian Mbaka</strong>, a passionate software developer specializing in creating user-friendly applications.</p>
            
            <div class="contact-buttons">
                <a href="https://wa.me/254703917940" class="contact-btn btn-whatsapp" target="_blank">
                    <i class="fab fa-whatsapp"></i> WhatsApp: +254703917940
                </a>
                <a href="tel:+254102273123" class="contact-btn btn-phone">
                    <i class="fas fa-phone"></i> Call: +254102273123
                </a>
                <a href="mailto:remotaskfreelancer@gmail.com" class="contact-btn btn-email">
                    <i class="fas fa-envelope"></i> Email: remotaskfreelancer@gmail.com
                </a>
            </div>
            
            <p>Check out my portfolio and other projects:</p>
            
            <div class="contact-buttons">
                <a href="https://github.com/brianmbakadev" class="contact-btn btn-portfolio" target="_blank">
                    <i class="fab fa-github"></i> GitHub Portfolio
                </a>
                <a href="https://afyasmartdoc.com" class="contact-btn btn-live" target="_blank">
                    <i class="fas fa-external-link-alt"></i> Live Demo
                </a>
            </div>
            
            <h2>License</h2>
            
            <p>This project is licensed under the MIT License - see the <a href="#">LICENSE</a> file for details.</p>
            
            <h2>Acknowledgments</h2>
            
            <ul>
                <li>Bootstrap for the responsive layout components</li>
                <li>Font Awesome for the beautiful icons</li>
                <li>Google Fonts for the typography</li>
                <li>All contributors who have helped improve AfyaSmart</li>
            </ul>
            
            <div class="alert alert-primary mt-4" role="alert">
                <i class="fas fa-info-circle me-2"></i> <strong>Disclaimer:</strong> AfyaSmart is not a substitute for professional medical advice. Always consult a healthcare professional for proper diagnosis and treatment of health conditions.
            </div>
        </article>
    </div>
    
    <footer class="footer">
        <div class="container">
            <p>Developed with <i class="fas fa-heart text-danger"></i> by Brian Mbaka</p>
            <p>© 2023 AfyaSmart Health Assistant. All rights reserved.</p>
        </div>
    </footer>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
