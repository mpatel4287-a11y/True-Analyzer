import random

# A robust bank of highly detailed, practical, budget-friendly problem-solving ideas
MOCK_IDEAS_BANK = {
    "Computer Science & IT": [
        {
            "title": "Low-Bandwidth Decentralized Communication Mesh",
            "tagline": "Ensuring connectivity when cellular networks fail.",
            "description": "In disaster zones or remote areas, standard internet infrastructure often collapses. This project uses a network of cheap ESP32 microcontrollers configured as a Bluetooth/Wi-Fi mesh to forward encrypted text messages between smartphones without any sim card or internet connection. Users connect to a local node via a web portal, type a message, and it hops across the mesh until it reaches the destination layer. It solves real-world communication crises and teaches essential networking practically.",
            "why_valuable": "Highly relevant for disaster recovery and remote communities. Very cheap to prototype.",
            "innovation_score": 8.5,
            "feasibility_score": 9.0,
            "market_need": "Significant global need for resilient communication in volatile regions.",
            "quick_wins": ["Establish peer-to-peer connection between two ESP32s", "Implement message hopping protocol", "Build lightweight web interface"],
            "core_components": ["ESP32 Microcontrollers (x3)", "Lithium-ion batteries", "Python / C++", "WebSockets"],
            "estimated_months": 3,
            "estimated_budget_usd": 45,
            "difficulty": "Intermediate"
        },
        {
            "title": "Smart Energy Consumption Tracker & AI Predictor",
            "tagline": "Helping households cut electricity costs through transparent insights.",
            "description": "A software-based dashboard integrated with inexpensive non-invasive current sensors (CT sensors) that clamp onto home breaker panels. The system logs electricity usage per circuit and uses a lightweight machine learning algorithm (like Random Forest) to identify specific appliances turning on and off by their energy signature. The app then predicts monthly bills and highlights phantom power drains, providing a highly practical, budget-friendly IoT analytics learning experience.",
            "why_valuable": "Directly tackles the rising cost of energy. Demonstrates high-value data analytics.",
            "innovation_score": 8.0,
            "feasibility_score": 8.5,
            "market_need": "Consumers strongly desire actionable ways to reduce utility bills.",
            "quick_wins": ["Read analog sensor data via ADC", "Stream data to cloud database", "Train ML classifier on appliance signatures"],
            "core_components": ["Raspberry Pi Pico W", "SCT-013 Current Sensors", "InfluxDB & Grafana", "Scikit-Learn"],
            "estimated_months": 4,
            "estimated_budget_usd": 65,
            "difficulty": "Advanced"
        },
        {
            "title": "AI-Powered Automated Code Reviewer Pipeline",
            "tagline": "Catching security flaws before they merge.",
            "description": "A pure software project that creates a Custom GitHub Action (or Git hook) that automatically parses incoming pull requests. Instead of just running standard linters, it uses local open-source Natural Language Processing models to flag logic errors and hardcoded secrets, then comments directly on the PR with suggested code diffs. This solves the major problem of expensive code reviews by streamlining the bottleneck securely and freely.",
            "why_valuable": "Teaches DevOps, CI/CD, and applied ML. Solves a major software engineering pain point.",
            "innovation_score": 7.5,
            "feasibility_score": 9.5,
            "market_need": "Every software team needs cheaper, faster, and more reliable code review processes.",
            "quick_wins": ["Set up webhook for Git pushes", "Parse diff payloads safely", "Integrate AST and logic rules"],
            "core_components": ["Python", "GitHub Actions / GitLab CI", "AST parsing libraries"],
            "estimated_months": 2,
            "estimated_budget_usd": 0,
            "difficulty": "Intermediate"
        },
        {
            "title": "Budget Automated Vertical Farming Controller",
            "tagline": "Maximizing crop yield in urban environments.",
            "description": "Urban space is scarce, and traditional agriculture uses immense water. This project creates a centralized controller software for hydroponic vertical farms. It orchestrates water pumps, grow lights, and pH dosers based on real-time environmental data (humidity, temperature, reservoir levels). The software includes a fault-tolerant state machine to ensure plants never dry out, using cheap microcontrollers and a central Python orchestrator.",
            "why_valuable": "Tackles food scarcity and sustainability in an engineering-focused, highly scalable way.",
            "innovation_score": 8.2,
            "feasibility_score": 8.8,
            "market_need": "Growing trend in urban agriculture requiring highly precise, inexpensive automation software.",
            "quick_wins": ["Read I2C sensors reliably", "Create fail-safe actuator toggles", "Build React frontend for remote monitoring"],
            "core_components": ["Python backend", "React UI", "Arduino Nano for I/O", "Relay modules"],
            "estimated_months": 5,
            "estimated_budget_usd": 120,
            "difficulty": "Advanced"
        }
    ],
    "Robotics & Automation": [
        {
            "title": "Autonomous Trash-Sorting Robotic Arm",
            "tagline": "Eliminating recycling contamination at the source.",
            "description": "A miniature, 3D-printable robotic arm stationed over a small conveyor belt. A standard webcam captures incoming waste items, and a lightweight YOLOv8 (computer vision) model running on a laptop or Raspberry Pi identifies whether the item is plastic, paper, or organic. The arm automatically intercepts non-recyclable items and drops them into a reject bin. This fundamentally solves recycling stream contamination cost-effectively.",
            "why_valuable": "Solves a critical environmental issue. Perfect blend of kinematics and modern computer vision.",
            "innovation_score": 8.8,
            "feasibility_score": 8.0,
            "market_need": "Recycling facilities spend millions manually sorting contaminated recycling bins.",
            "quick_wins": ["Assemble 3D printed arm joints", "Train custom YOLO vision model", "Bridge Python vision loop to Arduino serial"],
            "core_components": ["Standard Webcam", "Arduino Uno", "MG996R Servos", "OpenCV & PyTorch"],
            "estimated_months": 5,
            "estimated_budget_usd": 150,
            "difficulty": "Advanced"
        },
        {
            "title": "Warehouse Swarm Logistics Robot (Miniature)",
            "tagline": "Optimizing inventory retrieval with collaborative micro-bots.",
            "description": "Instead of one expensive robot, this project uses a swarm of three extremely cheap, identical two-wheeled robots (built using standard DC motors and ESP32s). They communicate over a local network to fulfill 'orders' by navigating a grid map marked with AruCo tags (QR codes for robots) on the floor. If one robot fails, the system automatically dispatches another. This tackles the complexities of swarm algorithms and multi-agent pathfinding on a student-friendly budget.",
            "why_valuable": "Swarm robotics is the future of Amazon-style logistics. Highly scalable and visually impressive.",
            "innovation_score": 9.0,
            "feasibility_score": 7.5,
            "market_need": "Warehouses worldwide need cheaper, redundant automation systems.",
            "quick_wins": ["Implement PID motor control for straight lines", "Read AruCo floor tags via downward camera", "Write central orchestrator Python server"],
            "core_components": ["ESP32-CAM modules", "L298N Motor Drivers", "Chassis kits", "Python WebSocket Server"],
            "estimated_months": 4,
            "estimated_budget_usd": 100,
            "difficulty": "Expert"
        }
    ],
    "Artificial Intelligence & ML": [
        {
            "title": "Edge-AI Medical Anomaly Detector",
            "tagline": "Diagnosing conditions instantly on low-power devices.",
            "description": "Medical data privacy is crucial, meaning sending x-rays or ECG data to the cloud is risky and slow. This project compresses a deep learning diagnostic model (e.g., detecting pneumonia from lung scans) using quantization so it fits entirely on a local mobile application or Raspberry Pi. It provides instant, offline, private diagnostics in rural or internet-deprived regions.",
            "why_valuable": "Solves data privacy and internet reliability issues in global health tech.",
            "innovation_score": 8.5,
            "feasibility_score": 8.0,
            "market_need": "Hospitals require low-latency, highly secure AI tools.",
            "quick_wins": ["Train base CNN model in cloud", "Apply TensorFlow Lite quantization", "Deploy and benchmark inference speed locally"],
            "core_components": ["TensorFlow Lite", "Keras", "Public Healthcare Datasets (Kaggle)", "Python"],
            "estimated_months": 3,
            "estimated_budget_usd": 0,
            "difficulty": "Advanced"
        },
        {
            "title": "Real-time Sign Language Translator",
            "tagline": "Bridging communication gaps seamlessly.",
            "description": "An application that uses a laptop or smartphone camera to capture hand gestures and translates them into text or speech in real time. Rather than relying on bulky sensor gloves, it uses Google MediaPipe for robust hand-tracking and skeletal joint data extraction, feeding those coordinates into a lightweight Recurrent Neural Network (RNN/LSTM) to classify dynamic gestures.",
            "why_valuable": "Creates massive accessibility improvements using entirely software-based, budget-friendly methods.",
            "innovation_score": 8.2,
            "feasibility_score": 8.5,
            "market_need": "High demand for inclusive digital accessibility software.",
            "quick_wins": ["Extract joint landmarks via MediaPipe", "Build custom dataset of video gestures", "Train LSTM sequence classifier"],
            "core_components": ["Python", "Google MediaPipe", "PyTorch / TensorFlow", "OpenCV"],
            "estimated_months": 4,
            "estimated_budget_usd": 0,
            "difficulty": "Intermediate"
        }
    ]
}

def get_detailed_mock_ideas(field: str, count: int = 6) -> list:
    # Get the specific ideas for the field, or fallback to CS if field is not exactly matched
    field_ideas = MOCK_IDEAS_BANK.get(field, [])
    if not field_ideas:
        # Provide general excellent ideas by pooling random ones
        pool = []
        for ideas in MOCK_IDEAS_BANK.values():
            pool.extend(ideas)
        field_ideas = pool
        
    # Shuffle and pad if needed
    random.shuffle(field_ideas)
    
    # We might not have 6, so duplicate or just return what we have (pad with general pool)
    result = field_ideas[:count]
    if len(result) < count:
        pool = []
        for ideas in MOCK_IDEAS_BANK.values():
             if ideas not in result:
                 pool.extend(ideas)
        random.shuffle(pool)
        for p in pool:
            if p not in result and len(result) < count:
                result.append(p)
                
    return result
