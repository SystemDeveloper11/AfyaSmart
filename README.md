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
    <!-- AOS Library for animations -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
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
            margin-bottom: 3rem;
            border-bottom: 5px solid var(--secondary-color);
        }
        
        .header h1 {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .content-container {
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            padding: 2.5rem;
            margin-bottom: 2rem;
        }
        
        h1, h2, h3, h4, h5 {
            font-family: 'Poppins', sans-serif;
            color: var(--primary-color);
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }
        
        h2 {
            border-bottom: 2px solid var(--secondary-color);
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
        }
        
        .feature-card {
            background: linear-gradient(to bottom right, #f8fafc, #f1f5f9);
            border-radius: 12px;
            padding: 1.5rem;
            height: 100%;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-left: 4px solid var(--primary-color);
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }
        
        .feature-icon {
            font-size: 2.5rem;
            color: var(--primary-color);
            margin-bottom: 1rem;
        }
        
        .contact-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 12px 25px;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s ease;
            margin: 0.5rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        
        .contact-btn i {
            margin-right: 10px;
            font-size: 1.2rem;
        }
        
        .btn-whatsapp {
            background: linear-gradient(120deg, #25D366, #128C7E);
            color: white;
        }
        
        .btn-whatsapp:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(37, 211, 102, 0.3);
            color: white;
        }
        
        .btn-phone {
            background: linear-gradient(120deg, var(--primary-color), #6c8ef5);
            color: white;
        }
        
        .btn-phone:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(78, 115, 223, 0.3);
            color: white;
        }
        
        .btn-email {
            background: linear-gradient(120deg, #EA4335, #D14836);
            color: white;
        }
        
        .btn-email:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(234, 67, 53, 0.3);
            color: white;
        }
        
        .btn-portfolio {
            background: linear-gradient(120deg, var(--secondary-color), #17a673);
            color: white;
        }
        
        .btn-portfolio:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(28, 200, 138, 0.3);
            color: white;
        }
        
        .btn-live {
            background: linear-gradient(120deg, #FF6B6B, #FF8E8E);
            color: white;
        }
        
        .btn-live:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(255, 107, 107, 0.3);
            color: white;
        }
        
        .tech-badge {
            display: inline-block;
            background: linear-gradient(to right, #edf2f7, #e2e8f0);
            color: var(--dark-color);
            padding: 5px 15px;
            border-radius: 20px;
            margin: 0.3rem;
            font-size: 0.9rem;
            font-weight: 500;
            border: 1px solid #cbd5e0;
        }
        
        .screenshot {
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease;
        }
        
        .screenshot:hover {
            transform: scale(1.02);
        }
        
        .footer {
            background: var(--dark-color);
            color: white;
            padding: 2rem 0;
            margin-top: 3rem;
        }
        
        .highlight {
            background: linear-gradient(120deg, rgba(78, 115, 223, 0.1), rgba(28, 200, 138, 0.1));
            padding: 2rem;
            border-radius: 10px;
            margin: 1.5rem 0;
            border-left: 4px solid var(--primary-color);
        }
        
        code {
            background: #f1f5f9;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Fira Code', monospace;
            color: var(--primary-color);
        }
        
        pre {
            background: #2d3748;
            color: #e2e8f0;
            padding: 1.5rem;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1.5rem 0;
        }
        
        .logo {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 1rem;
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2.2rem;
            }
            
            .header p {
                font-size: 1rem;
            }
            
            .content-container {
                padding: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header class="header text-center">
        <div class="container">
            <div class="logo">AfyaSmart</div>
            <h1>AfyaSmart Health Assistant</h1>
            <p>An intelligent health assistant that provides symptom analysis, health recommendations, and medication guidance</p>
            <p>Developed by <strong>Brian Mbaka</strong></p>
        </div>
    </header>

    <!-- Main Content -->
    <div class="container">
        <!-- Introduction -->
        <div class="content-container" data-aos="fade-up">
            <h2>Overview</h2>
            <p>AfyaSmart is an advanced health assistant designed to provide users with immediate health guidance based on their described symptoms. The application offers potential diagnoses, actionable recommendations, and medication information in an easy-to-understand format.</p>
            
            <div class="highlight">
                <p>AfyaSmart is built with a focus on user experience and medical accuracy, providing valuable health information while always reminding users to consult healthcare professionals for serious conditions.</p>
            </div>
        </div>

        <!-- Features -->
        <div class="content-container" data-aos="fade-up" data-aos-delay="100">
            <h2>Key Features</h2>
            <div class="row">
                <div class="col-md-4 mb-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-diagnoses"></i>
                        </div>
                        <h4>Symptom Analysis</h4>
                        <p>Provides potential health issues based on user-described symptoms with 4 possible conditions.</p>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-tasks"></i>
                        </div>
                        <h4>Actionable Recommendations</h4>
                        <p>Offers clear, point-form advice on what users should do to alleviate their symptoms.</p>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-capsules"></i>
                        </div>
                        <h4>Medication Guidance</h4>
                        <p>Provides information about potential medications, including dosage and usage instructions.</p>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-exclamation-triangle"></i>
                        </div>
                        <h4>Warning System</h4>
                        <p>Alerts users when they should seek immediate medical attention based on their symptoms.</p>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-user-md"></i>
                        </div>
                        <h4>User-Friendly Interface</h4>
                        <p>Clean, modern design with intuitive navigation and responsive layout for all devices.</p>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-comment-medical"></i>
                        </div>
                        <h4>Interactive Chat</h4>
                        <p>Engaging chat interface with typing indicators and quick suggestion buttons.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Technology Stack -->
        <div class="content-container" data-aos="fade-up" data-aos-delay="200">
            <h2>Technology Stack</h2>
            <p>AfyaSmart is built with modern web technologies to ensure performance, security, and scalability:</p>
            
            <div class="text-center my-4">
                <span class="tech-badge">HTML5</span>
                <span class="tech-badge">CSS3</span>
                <span class="tech-badge">JavaScript</span>
                <span class="tech-badge">Bootstrap 5</span>
                <span class="tech-badge">Font Awesome</span>
                <span class="tech-badge">Google Fonts</span>
                <span class="tech-badge">AOS Animations</span>
            </div>
            
            <p>The application features a responsive design that works seamlessly on desktop, tablet, and mobile devices.</p>
        </div>

        <!-- Installation -->
        <div class="content-container" data-aos="fade-up" data-aos-delay="300">
            <h2>Installation</h2>
            <p>To run AfyaSmart locally, follow these steps:</p>
            
            <pre><code># Clone the repository
git clone https://github.com/brianmbakadev/afyasmart.git

# Navigate to the project directory
cd afyasmart

# Open index.html in your browser
# Alternatively, use a local server for better performance
python -m http.server 8000</code></pre>
            
            <p>Then open your browser and navigate to <code>http://localhost:8000</code> to view the application.</p>
        </div>

        <!-- Usage -->
        <div class="content-container" data-aos="fade-up" data-aos-delay="400">
            <h2>Usage</h2>
            <p>Using AfyaSmart is simple and intuitive:</p>
            <ol>
                <li>Enter your name when prompted for a personalized experience</li>
                <li>Describe your symptoms in the chat interface</li>
                <li>Receive a comprehensive health assessment with possible conditions</li>
                <li>Review the recommended actions and medication guidance</li>
                <li>Follow the advice or seek professional medical help if warnings appear</li>
            </ol>
            
            <div class="highlight">
                <p><strong>Note:</strong> AfyaSmart is designed for informational purposes only and does not replace professional medical advice. Always consult a healthcare provider for accurate diagnosis and treatment.</p>
            </div>
        </div>

        <!-- Contact Section -->
        <div class="content-container text-center" data-aos="fade-up" data-aos-delay="500">
            <h2>Contact the Developer</h2>
            <p>Feel free to reach out for questions, collaborations, or feedback</p>
            
            <div class="d-flex flex-wrap justify-content-center mt-4">
                <a href="https://wa.me/254703917940" class="contact-btn btn-whatsapp">
                    <i class="fab fa-whatsapp"></i> WhatsApp
                </a>
                
                <a href="tel:+254102273123" class="contact-btn btn-phone">
                    <i class="fas fa-phone"></i> Call
                </a>
                
                <a href="mailto:remotaskfreelancer@gmail.com" class="contact-btn btn-email">
                    <i class="fas fa-envelope"></i> Email
                </a>
                
                <a href="https://github.com/brianmbakadev" class="contact-btn btn-portfolio">
                    <i class="fab fa-github"></i> Portfolio
                </a>
                
                <a href="https://afyasmartdoc.com" class="contact-btn btn-live">
                    <i class="fas fa-external-link-alt"></i> Live Demo
                </a>
            </div>
        </div>

        <!-- Screenshots -->
        <div class="content-container" data-aos="fade-up" data-aos-delay="600">
            <h2>Screenshots</h2>
            <div class="row">
                <div class="col-md-6">
                    <div class="screenshot">
                        <img src="https://via.placeholder.com/600x400/4e73df/ffffff?text=AfyaSmart+Chat+Interface" class="img-fluid" alt="AfyaSmart Chat Interface">
                    </div>
                    <p class="text-center"><strong>Chat Interface</strong></p>
                </div>
                <div class="col-md-6">
                    <div class="screenshot">
                        <img src="https://via.placeholder.com/600x400/1cc88a/ffffff?text=Health+Assessment" class="img-fluid" alt="Health Assessment">
                    </div>
                    <p class="text-center"><strong>Health Assessment</strong></p>
                </div>
            </div>
        </div>

        <!-- License -->
        <div class="content-container" data-aos="fade-up" data-aos-delay="700">
            <h2>License</h2>
            <p>This project is licensed under the MIT License - see the <a href="#">LICENSE.md</a> file for details.</p>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer text-center">
        <div class="container">
            <p>Developed with <i class="fas fa-heart" style="color: #ff6b6b;"></i> by Brian Mbaka</p>
            <p>© 2023 AfyaSmart Health Assistant. All rights reserved.</p>
        </div>
    </footer>

    <!-- AOS Animation Library -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        // Initialize AOS animation library
        AOS.init({
            duration: 1000,
            once: true,
            offset: 100
        });
    </script>
</body>
</html>
