from __future__ import annotations

import math
import re
from typing import Any


# ─── Field definitions ────────────────────────────────────────────────────────

FIELDS: dict[str, dict[str, Any]] = {
    # Engineering
    "Computer Science & IT": {
        "base_budget": 22000,
        "hourly_dev_rate": 40,
        "components": ["Backend API server", "Frontend UI", "Database layer", "Auth & user management", "CI/CD pipeline"],
        "requirements": ["System architecture diagram", "API documentation", "Unit & integration tests", "Cloud deployment plan"],
        "applications": ["Web/mobile applications", "SaaS platforms", "Developer tools", "Automation scripts"],
        "default_stack": ["Python / Node.js", "React / Vue", "PostgreSQL / MongoDB", "Docker", "GitHub Actions"],
    },
    "Artificial Intelligence & ML": {
        "base_budget": 35000,
        "hourly_dev_rate": 55,
        "components": ["Data ingestion pipeline", "Feature engineering module", "Model training framework", "Model serving API", "Monitoring dashboard"],
        "requirements": ["Labelled training dataset", "Evaluation metrics (accuracy, F1, AUC)", "MLOps workflow", "GPU/cloud compute budget"],
        "applications": ["Predictive analytics", "NLP tools", "Computer vision systems", "Recommendation engines"],
        "default_stack": ["Python", "PyTorch / TensorFlow", "scikit-learn", "FastAPI", "MLflow / W&B"],
    },
    "Electronics & Communication": {
        "base_budget": 18000,
        "hourly_dev_rate": 35,
        "components": ["Microcontroller/FPGA unit", "Signal processing module", "RF/wireless communication layer", "Power supply circuit", "PCB design"],
        "requirements": ["Hardware prototyping kit", "Signal simulation software", "Spectrum analyzer access", "EMI compliance testing"],
        "applications": ["Embedded systems", "IoT sensor networks", "5G/wireless prototypes", "Smart home devices"],
        "default_stack": ["C / C++", "Arduino / STM32", "MATLAB/Simulink", "Altium / KiCad (PCB)", "Zigbee / LoRa"],
    },
    "Electrical Engineering": {
        "base_budget": 25000,
        "hourly_dev_rate": 38,
        "components": ["Power electronics module", "Control system", "Simulation environment", "Monitoring & protection circuit", "HMI interface"],
        "requirements": ["Lab equipment (oscilloscope, multimeter)", "MATLAB/Simulink license", "Safety certification", "Grid integration study"],
        "applications": ["Renewable energy systems", "Motor drive controllers", "Smart grid solutions", "Battery management systems"],
        "default_stack": ["MATLAB/Simulink", "PSIM / PLECS", "LabVIEW", "C (embedded)", "AutoCAD Electrical"],
    },
    "Mechanical Engineering": {
        "base_budget": 20000,
        "hourly_dev_rate": 35,
        "components": ["CAD/CAM model", "FEA simulation", "Prototype fabrication", "Testing rig", "Material selection report"],
        "requirements": ["3D printer / CNC access", "Material testing lab", "Thermal/structural analysis software", "Manufacturing process plan"],
        "applications": ["Automotive components", "Robotics mechanisms", "HVAC systems", "Industrial machinery"],
        "default_stack": ["SolidWorks / CATIA", "ANSYS / Abaqus (FEA)", "AutoCAD", "MATLAB", "GD&T tooling"],
    },
    "Civil & Structural Engineering": {
        "base_budget": 30000,
        "hourly_dev_rate": 38,
        "components": ["Structural analysis model", "BIM/CAD drawings", "Site survey data", "Load calculation report", "Cost estimation sheet"],
        "requirements": ["AutoCAD / Revit license", "Geotechnical survey", "Building code compliance", "Environmental impact assessment"],
        "applications": ["Smart buildings", "Bridge/dam design", "Urban planning tools", "Disaster-resistant structures"],
        "default_stack": ["AutoCAD / Revit", "STAAD.Pro / ETABS", "SAP2000", "ArcGIS", "MS Project"],
    },
    "Robotics & Automation": {
        "base_budget": 40000,
        "hourly_dev_rate": 50,
        "components": ["Actuator & sensor array", "Robot controller", "Path planning algorithm", "Simulation environment (ROS/Gazebo)", "Safety interlock system"],
        "requirements": ["Robotic hardware kit", "ROS/ROS2 framework", "Real-time OS", "Collision detection testing"],
        "applications": ["Industrial automation", "Surgical robots", "Autonomous drones", "Warehouse logistics robots"],
        "default_stack": ["ROS2", "Python / C++", "Gazebo / Webots", "OpenCV", "Arduino / Raspberry Pi"],
    },
    "IoT & Embedded Systems": {
        "base_budget": 15000,
        "hourly_dev_rate": 35,
        "components": ["Microcontroller (Arduino/ESP32/RPi)", "Sensor suite", "Wireless communication module", "Cloud IoT gateway", "Edge processing unit"],
        "requirements": ["Embedded C/Python firmware", "Low-power design", "OTA update mechanism", "Security hardening"],
        "applications": ["Smart agriculture sensors", "Wearable health monitors", "Smart city infrastructure", "Industrial telemetry"],
        "default_stack": ["C / MicroPython", "ESP32 / STM32", "MQTT / CoAP", "AWS IoT / Azure IoT Hub", "FreeRTOS"],
    },
    "Cybersecurity": {
        "base_budget": 28000,
        "hourly_dev_rate": 55,
        "components": ["Threat detection engine", "SIEM integration", "Vulnerability scanner", "Incident response playbook", "Secure logging layer"],
        "requirements": ["Penetration testing scope", "CVE database access", "Compliance framework (ISO 27001 / SOC2)", "Isolated lab environment"],
        "applications": ["Intrusion detection systems", "Zero-trust network tools", "Malware analysis platforms", "Secure coding assistants"],
        "default_stack": ["Python", "Wireshark / Zeek", "Metasploit / Burp Suite", "ELK Stack", "Snort / Suricata"],
    },
    "Data Science & Analytics": {
        "base_budget": 18000,
        "hourly_dev_rate": 45,
        "components": ["Data warehouse", "ETL pipeline", "Exploratory analysis notebooks", "Visualization dashboard", "Statistical model"],
        "requirements": ["Clean, representative dataset", "BI tool (Tableau/Power BI)", "Statistical validation plan", "Data governance policy"],
        "applications": ["Business intelligence dashboards", "Customer churn analysis", "Sports analytics", "Scientific research analysis"],
        "default_stack": ["Python (pandas, numpy)", "Jupyter Notebook", "SQL / dbt", "Power BI / Tableau", "Apache Spark"],
    },
    "Chemical Engineering": {
        "base_budget": 30000,
        "hourly_dev_rate": 40,
        "components": ["Process simulation model", "Reactor design module", "Safety & hazard analysis", "Pilot plant setup", "Quality control system"],
        "requirements": ["ASPEN / HYSYS license", "Lab chemicals & safety gear", "Process flow diagram (PFD)", "Environmental compliance plan"],
        "applications": ["Drug manufacturing processes", "Green chemistry solutions", "Petrochemical optimization", "Food processing automation"],
        "default_stack": ["Aspen HYSYS / Plus", "MATLAB", "Python (CoolProp)", "AutoCAD P&ID", "HAZOP software"],
    },
    "Biomedical Engineering": {
        "base_budget": 55000,
        "hourly_dev_rate": 50,
        "components": ["Biosensor / medical device", "Signal acquisition module", "Clinical data pipeline", "Regulatory compliance module", "User interface for clinicians"],
        "requirements": ["FDA/CE medical device standards", "Clinical trial protocol", "Biocompatibility testing", "HIPAA data handling"],
        "applications": ["Wearable health monitors", "Prosthetics & implants", "Diagnostic imaging tools", "Telemedicine devices"],
        "default_stack": ["Python / MATLAB", "LabVIEW (DAQ)", "C++ (embedded medical)", "DICOM / HL7", "TensorFlow Lite"],
    },
    "Aerospace Engineering": {
        "base_budget": 80000,
        "hourly_dev_rate": 60,
        "components": ["Aerodynamic simulation (CFD)", "Structural design model", "Propulsion system", "Navigation & control system", "Ground control station"],
        "requirements": ["CFD software (ANSYS Fluent)", "Wind tunnel / test facility", "FAA/DGCA compliance", "Avionics integration plan"],
        "applications": ["UAV/drone systems", "Satellite subsystems", "Aircraft component design", "Space habitat modules"],
        "default_stack": ["ANSYS Fluent / OpenFOAM", "MATLAB/Simulink", "Python (AeroSandbox)", "C++ (flight software)", "OpenRocket"],
    },
    "Environmental Engineering": {
        "base_budget": 22000,
        "hourly_dev_rate": 38,
        "components": ["Pollution monitoring sensors", "GIS mapping layer", "Environmental model", "Reporting portal", "Remediation planner"],
        "requirements": ["Field data collection plan", "GIS / remote sensing tools", "EPA/NGT compliance", "Stakeholder engagement plan"],
        "applications": ["Air/water quality monitoring", "Waste management systems", "Climate impact modelling", "Green energy auditing"],
        "default_stack": ["Python (GeoPandas)", "ArcGIS / QGIS", "MATLAB", "R (statistics)", "EPA SWMM / WASP"],
    },
    "Game Development": {
        "base_budget": 25000,
        "hourly_dev_rate": 40,
        "components": ["Game engine setup", "Physics & collision system", "Asset pipeline (art/audio)", "Multiplayer/networking layer", "UI/UX & HUD"],
        "requirements": ["Game design document (GDD)", "Art asset pack or artist", "Platform SDKs (Steam/iOS/Android)", "QA testing plan"],
        "applications": ["Indie PC/console games", "Mobile games", "Serious games for training", "VR/AR experiences"],
        "default_stack": ["Unity / Unreal Engine", "C# / C++ / Blueprints", "Blender (3D assets)", "Photon (multiplayer)", "Steam SDK"],
    },
    "AR / VR & Metaverse": {
        "base_budget": 45000,
        "hourly_dev_rate": 55,
        "components": ["XR rendering engine", "Spatial tracking module", "3D asset pipeline", "Interaction/gesture system", "Cloud sync layer"],
        "requirements": ["AR/VR headset hardware", "Spatial computing SDK", "Low-latency network (<20ms)", "3D content authoring pipeline"],
        "applications": ["Virtual classrooms", "AR product visualization", "VR therapy/training", "Metaverse social spaces"],
        "default_stack": ["Unity / Unreal", "ARKit / ARCore / WebXR", "Blender / Maya", "Oculus SDK / OpenXR", "WebGL / Three.js"],
    },
    "Blockchain & Web3": {
        "base_budget": 35000,
        "hourly_dev_rate": 60,
        "components": ["Smart contract layer", "On-chain data indexer", "Wallet integration", "Frontend dApp", "Token economics module"],
        "requirements": ["Blockchain platform choice (Ethereum/Solana)", "Security audit", "Gas fee optimization plan", "Legal/regulatory review"],
        "applications": ["Decentralized finance (DeFi)", "NFT marketplaces", "Supply chain traceability", "DAO governance tools"],
        "default_stack": ["Solidity / Rust", "Hardhat / Anchor", "ethers.js / web3.js", "React (dApp)", "IPFS / Filecoin"],
    },
    # Other domains
    "Healthcare": {
        "base_budget": 65000,
        "hourly_dev_rate": 50,
        "components": ["Clinical data pipeline", "Compliance module", "Model monitoring", "User dashboard", "EHR integration"],
        "requirements": ["HIPAA compliance", "Medical advisor", "Data privacy controls", "Clinical validation study"],
        "applications": ["Early risk detection", "Remote patient triage", "Hospital workflow optimization", "Drug discovery support"],
        "default_stack": ["Python / Java", "HL7 FHIR API", "TensorFlow / PyTorch", "PostgreSQL", "AWS HIPAA-eligible services"],
    },
    "Education & EdTech": {
        "base_budget": 20000,
        "hourly_dev_rate": 38,
        "components": ["Learning engine", "Progress analytics", "Content recommender", "Instructor portal", "Assessment module"],
        "requirements": ["Curriculum mapping", "Assessment dataset", "Accessibility support (WCAG 2.1)", "LMS integration (Moodle/Canvas)"],
        "applications": ["Personalized learning paths", "Dropout prediction", "Adaptive tutoring", "Skill gap analysis"],
        "default_stack": ["React / Next.js", "Python (FastAPI)", "PostgreSQL", "OpenAI API", "AWS / Firebase"],
    },
    "Finance & Fintech": {
        "base_budget": 50000,
        "hourly_dev_rate": 60,
        "components": ["Risk scoring model", "Fraud detector", "Audit logs", "Secure API gateway", "Payment processor integration"],
        "requirements": ["KYC/AML checks", "PCI-DSS compliance", "Security penetration test", "Regulatory reporting"],
        "applications": ["Fraud prevention", "Credit scoring", "Algorithmic trading", "Personal finance management"],
        "default_stack": ["Python / Java", "Kafka (streaming)", "Spark (analytics)", "Kubernetes", "Stripe / Plaid API"],
    },
    "Agriculture & AgriTech": {
        "base_budget": 20000,
        "hourly_dev_rate": 35,
        "components": ["Sensor ingestion", "Prediction model", "Farmer mobile app", "Alerting service", "Satellite imagery module"],
        "requirements": ["Field pilot data", "IoT connectivity", "Offline-first UX", "Local language support"],
        "applications": ["Yield forecasting", "Pest & disease prediction", "Smart irrigation", "Supply chain traceability"],
        "default_stack": ["Python", "TensorFlow Lite (edge)", "React Native", "MQTT", "Google Earth Engine"],
    },
    "Manufacturing & Industry 4.0": {
        "base_budget": 45000,
        "hourly_dev_rate": 45,
        "components": ["Machine telemetry collector", "Anomaly detector", "Maintenance scheduler", "Digital twin", "Operations dashboard"],
        "requirements": ["OPC-UA / MQTT factory integration", "Edge deployment plan", "Latency SLAs", "Safety standards (IEC 61508)"],
        "applications": ["Predictive maintenance", "Computer vision quality inspection", "Digital twin simulation", "Supply chain optimization"],
        "default_stack": ["Python", "OPC-UA / MQTT", "InfluxDB (time-series)", "Grafana", "TensorFlow / ONNX"],
    },
    "Retail & E-Commerce": {
        "base_budget": 25000,
        "hourly_dev_rate": 40,
        "components": ["Demand forecasting", "Recommendation engine", "Inventory optimizer", "Customer analytics", "A/B testing module"],
        "requirements": ["POS/ERP integration", "Customer consent (GDPR)", "MLOps pipeline", "Real-time event tracking"],
        "applications": ["Personalized product recommendations", "Dynamic pricing", "Customer churn prevention", "Visual search"],
        "default_stack": ["Python", "Spark / Flink (streaming)", "PostgreSQL / Redis", "React (storefront)", "Segment / Amplitude"],
    },
    "Sustainability & Clean Energy": {
        "base_budget": 28000,
        "hourly_dev_rate": 42,
        "components": ["Emission tracker", "Energy optimization model", "Reporting portal", "Carbon analytics layer", "Renewable integration module"],
        "requirements": ["ESG metrics alignment", "Third-party carbon verification", "Smart meter / grid API", "Regulatory reporting (GHG Protocol)"],
        "applications": ["Carbon footprint tracking", "Renewable energy forecasting", "Waste reduction planning", "Green building certification"],
        "default_stack": ["Python", "InfluxDB", "Grafana", "React", "AWS / Azure (green regions)"],
    },
    "Other / Custom": {
        "base_budget": 20000,
        "hourly_dev_rate": 40,
        "components": ["Data ingestion", "Core model / logic", "User management", "Insights dashboard", "API layer"],
        "requirements": ["Domain expert review", "Data quality checks", "Monitoring + alerting", "User acceptance testing"],
        "applications": ["Decision automation", "Forecasting", "Process optimization", "User-facing product"],
        "default_stack": ["Python / Node.js", "React", "PostgreSQL", "Docker", "Cloud hosting (AWS/GCP/Azure)"],
    },
}


# ─── Keyword signal banks ─────────────────────────────────────────────────────

# Raise feasibility
FEASIBILITY_BOOST = {
    "open source", "existing api", "off-the-shelf", "pretrained", "transfer learning",
    "proven", "well-documented", "standard", "simple", "prototype", "mvp",
    "cloud", "serverless", "microservice", "agile", "iterative", "modular",
}

# Lower feasibility / raise risk
COMPLEXITY_SIGNALS = {
    "real-time", "real time", "low latency", "sub-millisecond", "high frequency",
    "distributed", "federated", "multi-agent", "autonomous", "self-learning",
    "custom hardware", "fpga", "asic", "quantum", "neuromorphic",
    "regulation", "compliance", "fda", "hipaa", "gdpr", "ce mark", "faa",
    "clinical trial", "patent", "proprietary", "classified",
}

# Scale signals → affect budget + impact
SCALE_SIGNALS = {
    "global": 2.8, "worldwide": 2.8, "national": 2.0, "country-wide": 2.0,
    "city-wide": 1.5, "enterprise": 1.6, "100000": 1.5, "million users": 2.2,
    "large scale": 1.8, "mass deployment": 2.0, "at scale": 1.7,
    "regional": 1.3, "pilot": 0.7, "small scale": 0.7, "single user": 0.5,
    "single device": 0.5, "poc": 0.6, "proof of concept": 0.6,
}

# Hardware cost multipliers
HARDWARE_SIGNALS = {
    "drone": 8000, "robot": 12000, "sensor": 2000, "iot device": 3000,
    "raspberry pi": 80, "arduino": 40, "esp32": 15, "fpga": 5000,
    "camera": 300, "lidar": 4000, "gps module": 120, "motor": 200,
    "3d printer": 1500, "cnc": 8000, "spectrometer": 6000, "microscope": 3000,
    "server": 5000, "gpu": 2000, "edge device": 500,
}

# Cloud/infra cost signals (monthly)
CLOUD_SIGNALS = {
    "gpu training": 800, "deep learning": 600, "large language model": 900,
    "computer vision": 500, "real-time streaming": 400, "kubernetes": 350,
    "database cluster": 250, "cdn": 120, "api gateway": 80,
    "video processing": 600, "speech recognition": 300, "satellite data": 700,
}

# Regulatory cost additions
REGULATORY_SIGNALS = {
    "hipaa": 15000, "fda": 30000, "gdpr": 8000, "pci-dss": 12000,
    "iso 27001": 10000, "ce mark": 8000, "faa": 25000, "clinical trial": 50000,
    "medical device": 20000, "financial license": 20000, "patent": 12000,
}

# Innovation vocabulary
INNOVATION_SIGNALS = {
    "novel", "unique", "first-of-its-kind", "breakthrough", "patent",
    "ai-powered", "machine learning", "deep learning", "neural", "generative",
    "autonomous", "adaptive", "self-", "intelligent", "smart", "predictive",
    "llm", "gpt", "diffusion", "transformer", "graph neural", "multimodal",
    "blockchain", "quantum", "federated", "edge ai", "augmented reality",
    "virtual reality", "digital twin", "simulation",
}

# Tech stack hints — auto-suggest based on idea text
TECH_HINTS: list[tuple[set[str], str]] = [
    ({"react", "frontend", "web app", "ui", "dashboard", "portal"}, "React / Next.js"),
    ({"mobile", "android", "ios", "flutter", "react native"}, "React Native / Flutter"),
    ({"python", "django", "fastapi", "flask", "backend"}, "Python (FastAPI / Django)"),
    ({"node", "express", "javascript", "typescript", "js"}, "Node.js / Express"),
    ({"postgresql", "sql", "relational database", "mysql"}, "PostgreSQL / MySQL"),
    ({"mongodb", "nosql", "document store"}, "MongoDB"),
    ({"redis", "cache", "session"}, "Redis"),
    ({"docker", "container", "kubernetes", "k8s", "microservice"}, "Docker / Kubernetes"),
    ({"aws", "cloud", "lambda", "s3", "ec2"}, "AWS"),
    ({"gcp", "google cloud", "bigquery", "vertex"}, "Google Cloud Platform"),
    ({"azure", "microsoft cloud"}, "Microsoft Azure"),
    ({"tensorflow", "keras", "deep learning", "neural network", "cnn", "rnn"}, "TensorFlow / Keras"),
    ({"pytorch", "torch"}, "PyTorch"),
    ({"llm", "gpt", "openai", "chatgpt", "language model", "nlp", "text"}, "OpenAI API / LangChain"),
    ({"computer vision", "image", "video", "opencv", "yolo", "detection", "recognition"}, "OpenCV / YOLO"),
    ({"ros", "robot", "robotics", "gazebo"}, "ROS2 / Gazebo"),
    ({"iot", "mqtt", "sensor", "embedded", "microcontroller", "arduino", "esp32"}, "MQTT / FreeRTOS"),
    ({"blockchain", "smart contract", "solidity", "web3", "nft", "defi"}, "Solidity / ethers.js"),
    ({"spark", "kafka", "stream", "big data", "hadoop"}, "Apache Spark / Kafka"),
    ({"grafana", "monitoring", "metrics", "influx"}, "Grafana / InfluxDB"),
    ({"unity", "unreal", "game", "vr", "ar", "xr"}, "Unity / Unreal Engine"),
    ({"satellite", "gis", "mapping", "geospatial", "lidar"}, "ArcGIS / GeoPandas"),
]


# ─── Analyzer ─────────────────────────────────────────────────────────────────

class IdeaAnalyzer:

    def analyze(self, field: str, idea: str) -> dict[str, Any]:
        profile = FIELDS.get(field, FIELDS["Other / Custom"])
        idea_lower = idea.lower()
        idea_words = set(re.findall(r"[a-z0-9]+(?:[- ][a-z0-9]+)*", idea_lower))

        # ── Score signals ──────────────────────────────────────────────────
        feasibility_boost = sum(1 for kw in FEASIBILITY_BOOST if kw in idea_lower)
        complexity_hits = [kw for kw in COMPLEXITY_SIGNALS if kw in idea_lower]
        innovation_hits = [kw for kw in INNOVATION_SIGNALS if kw in idea_lower]
        hardware_hits = {hw: cost for hw, cost in HARDWARE_SIGNALS.items() if hw in idea_lower}
        cloud_hits = {svc: cost for svc, cost in CLOUD_SIGNALS.items() if svc in idea_lower}
        regulatory_hits = {reg: cost for reg, cost in REGULATORY_SIGNALS.items() if reg in idea_lower}

        scale_multiplier = 1.0
        scale_label = "Medium"
        for kw, mult in SCALE_SIGNALS.items():
            if kw in idea_lower:
                if mult > scale_multiplier:
                    scale_multiplier = mult
                    scale_label = kw.title()

        # Word count signals
        word_count = len(idea.split())
        detail_bonus = min(1.5, word_count / 80)  # more detail → better scores

        # ── Raw scores ────────────────────────────────────────────────────
        feasibility = min(9.5, max(2.5,
            6.0
            + feasibility_boost * 0.4
            - len(complexity_hits) * 0.35
            + detail_bonus * 0.5
            - (1.2 if regulatory_hits else 0)
            - (0.8 if len(hardware_hits) > 2 else 0)
        ))

        innovation = min(9.8, max(2.0,
            5.0
            + len(innovation_hits) * 0.55
            + (1.0 if len(innovation_hits) >= 3 else 0)
            + detail_bonus * 0.3
            - (0.5 if feasibility_boost > 3 else 0)  # very standard → less novel
        ))

        risk = min(9.5, max(1.5,
            3.5
            + len(complexity_hits) * 0.5
            + (len(regulatory_hits) * 0.6)
            + (0.8 if len(hardware_hits) > 1 else 0)
            + (scale_multiplier - 1.0) * 0.4
        ))

        impact = min(9.8, max(2.0,
            5.5
            + (scale_multiplier - 1.0) * 0.9
            + len(innovation_hits) * 0.2
            + detail_bonus * 0.4
        ))

        complexity = min(9.5, max(1.5,
            3.5
            + len(complexity_hits) * 0.55
            + len(hardware_hits) * 0.3
            + len(cloud_hits) * 0.25
            + (scale_multiplier - 1.0) * 0.35
        ))

        rating = round(
            feasibility * 0.30
            + innovation * 0.25
            + impact * 0.25
            - risk * 0.20,
            2,
        )
        rating = round(min(10.0, max(1.0, rating)), 2)

        # ── Budget calculation ─────────────────────────────────────────────
        base = profile["base_budget"]
        rate = profile["hourly_dev_rate"]

        # Dev months → hours
        dev_months = max(2, int(3 + complexity * 1.4))
        dev_hours = dev_months * 160  # 160h/month
        dev_cost = dev_hours * rate * scale_multiplier

        hardware_cost = sum(hardware_hits.values()) * 1.4  # 40% buffer
        cloud_monthly = sum(cloud_hits.values()) if cloud_hits else 120
        cloud_cost = cloud_monthly * dev_months * 1.2
        regulatory_cost = sum(regulatory_hits.values())
        contingency = (dev_cost + hardware_cost + cloud_cost + regulatory_cost) * 0.12

        total_budget = base + dev_cost + hardware_cost + cloud_cost + regulatory_cost + contingency

        budget_breakdown = {
            "Development (labour)": round(dev_cost, 0),
            "Hardware / Prototyping": round(hardware_cost, 0) if hardware_cost else round(base * 0.05, 0),
            "Cloud & Infrastructure": round(cloud_cost, 0),
            "Regulatory & Legal": round(regulatory_cost, 0) if regulatory_cost else round(base * 0.03, 0),
            "Testing & QA": round(total_budget * 0.08, 0),
            "Contingency (12%)": round(contingency, 0),
        }
        total_budget = sum(budget_breakdown.values())

        # ── Difficulty ─────────────────────────────────────────────────────
        diff_score = len(complexity_hits) + len(hardware_hits) + len(regulatory_hits) * 2
        if diff_score <= 1:
            difficulty = "Beginner"
            diff_color = "green"
        elif diff_score <= 3:
            difficulty = "Intermediate"
            diff_color = "blue"
        elif diff_score <= 6:
            difficulty = "Advanced"
            diff_color = "orange"
        else:
            difficulty = "Expert"
            diff_color = "red"

        # ── Timeline breakdown ─────────────────────────────────────────────
        phase_months = {
            "Research & Planning": max(1, round(dev_months * 0.15)),
            "Design & Architecture": max(1, round(dev_months * 0.20)),
            "Core Development": max(2, round(dev_months * 0.40)),
            "Testing & Integration": max(1, round(dev_months * 0.15)),
            "Deployment & Review": max(1, round(dev_months * 0.10)),
        }

        # ── Pros (dynamic, based on signals) ──────────────────────────────
        pros = []

        if feasibility >= 7:
            pros.append(f"High feasibility ({feasibility:.1f}/10) — core idea is technically achievable with available tools.")
        elif feasibility >= 5:
            pros.append(f"Moderate feasibility ({feasibility:.1f}/10) — achievable with focused effort and right tech choices.")

        if innovation >= 7:
            pros.append(f"Strong innovation score ({innovation:.1f}/10) — idea shows genuine novelty in the {field} space.")
        elif innovation >= 5.5:
            pros.append(f"Decent innovation level ({innovation:.1f}/10) — differentiating features exist.")

        if impact >= 7:
            pros.append(f"High potential impact ({impact:.1f}/10) — addresses a real problem with broad applicability.")

        if scale_multiplier >= 1.5:
            pros.append(f"Large target scale ('{scale_label}') creates significant market opportunity.")

        if innovation_hits:
            pros.append(f"Uses cutting-edge technology signals: {', '.join(list(innovation_hits)[:4])}.")

        if feasibility_boost >= 2:
            pros.append("Leverages proven/open-source tools, reducing development time and cost.")

        if not pros:
            pros.append("Idea addresses a real-world problem worth solving.")
            pros.append("Field has active community and learning resources.")

        # ── Cons (dynamic) ─────────────────────────────────────────────────
        cons = []

        if risk >= 6:
            cons.append(f"High risk score ({risk:.1f}/10) — needs a dedicated risk mitigation plan before starting.")
        elif risk >= 4:
            cons.append(f"Moderate risk ({risk:.1f}/10) — some uncertainties to address in early phases.")

        if complexity_hits:
            cons.append(f"Technical complexity factors detected: {', '.join(complexity_hits[:3])} — these require specialist expertise.")

        if regulatory_hits:
            cons.append(f"Regulatory requirements detected ({', '.join(list(regulatory_hits.keys())[:3])}) — adds cost, timeline, and legal overhead.")

        if hardware_hits:
            cons.append(f"Hardware dependency ({', '.join(list(hardware_hits.keys())[:3])}) — physical components can delay development and increase failure risk.")

        if scale_multiplier >= 2.0:
            cons.append("Global/national scale ambition adds significant infrastructure and operational complexity.")

        if word_count < 40:
            cons.append("Idea is described too briefly — more detail would improve accuracy of this analysis.")

        if not cons:
            cons.append("Budget estimation may vary significantly based on team experience and chosen tech stack.")
            cons.append("Market competition should be researched before committing to full development.")

        # ── Key Challenges (idea-specific) ─────────────────────────────────
        challenges = []
        if "real-time" in idea_lower or "real time" in idea_lower:
            challenges.append("Real-time processing requires optimised algorithms and low-latency infrastructure.")
        if "data" in idea_lower and ("privacy" in idea_lower or "personal" in idea_lower):
            challenges.append("User data privacy must be designed in from day one — encryption, anonymisation, consent.")
        if hardware_hits:
            challenges.append(f"Hardware procurement and integration: {', '.join(list(hardware_hits.keys())[:2])}.")
        if regulatory_hits:
            challenges.append(f"Navigating {', '.join(list(regulatory_hits.keys())[:2])} compliance will require legal consultation.")
        if "ai" in idea_lower or "ml" in idea_lower or "machine learning" in idea_lower:
            challenges.append("Model accuracy and bias must be continuously evaluated on real-world data.")
        if scale_multiplier >= 1.8:
            challenges.append("Scaling infrastructure to handle large user/data volume without outages.")
        if "mobile" in idea_lower or "android" in idea_lower or "ios" in idea_lower:
            challenges.append("Cross-platform UX consistency and App Store / Play Store review process.")
        if not challenges:
            challenges.append("Defining clear success metrics before development starts.")
            challenges.append("Building or sourcing a sufficient and representative dataset.")

        # ── Suggested tech stack (idea-aware) ─────────────────────────────
        suggested_stack = []
        for keyword_set, tech in TECH_HINTS:
            if any(kw in idea_lower for kw in keyword_set):
                if tech not in suggested_stack:
                    suggested_stack.append(tech)

        # Fallback to field default if nothing detected
        if len(suggested_stack) < 2:
            suggested_stack = profile.get("default_stack", [])
        else:
            # Merge unique field defaults
            for t in profile.get("default_stack", []):
                if t not in suggested_stack:
                    suggested_stack.append(t)
        suggested_stack = suggested_stack[:7]

        # ── Market opportunity ─────────────────────────────────────────────
        if scale_multiplier >= 2.5:
            market_size = "Very Large (>$10B TAM)"
            market_note = "Addresses a massive global market with room for multiple winners."
        elif scale_multiplier >= 1.8:
            market_size = "Large ($1B–$10B TAM)"
            market_note = "Significant market exists; early-mover advantage is important."
        elif scale_multiplier >= 1.3:
            market_size = "Medium ($100M–$1B TAM)"
            market_note = "Niche but profitable segment; focus on a specific vertical first."
        else:
            market_size = "Small / Local (<$100M TAM)"
            market_note = "Ideal for a focused MVP or academic/research project. Validate demand early."

        # ── Real-world applications (field + idea signals) ─────────────────
        applications = list(profile["applications"])
        if "predict" in idea_lower or "forecast" in idea_lower:
            applications.append("Operational forecasting & early warning systems")
        if "automat" in idea_lower:
            applications.append("Process automation & workflow optimisation")
        if "monitor" in idea_lower:
            applications.append("Continuous monitoring & anomaly alerting")
        if "detect" in idea_lower:
            applications.append("Automated detection & classification")
        if "recommend" in idea_lower:
            applications.append("Personalised recommendations & guidance")
        applications = list(dict.fromkeys(applications))[:6]

        # ── Components (field base + detected from idea) ────────────────────
        components = list(profile["components"])
        if any(t in idea_lower for t in ["mobile", "android", "ios"]):
            components.append("Mobile application (iOS / Android)")
        if any(t in idea_lower for t in ["iot", "sensor", "device", "embedded"]):
            components.append("IoT / edge data connector")
        if any(t in idea_lower for t in ["chat", "assistant", "llm", "gpt", "agent"]):
            components.append("LLM / NLP serving layer")
        if any(t in idea_lower for t in ["dashboard", "analytics", "report"]):
            components.append("Analytics & reporting dashboard")
        if any(t in idea_lower for t in ["payment", "subscription", "billing"]):
            components.append("Payment & billing integration")
        if any(t in idea_lower for t in ["map", "gis", "location", "geospatial"]):
            components.append("Geospatial / mapping layer")
        components = list(dict.fromkeys(components))[:8]

        # ── Requirements ───────────────────────────────────────────────────
        requirements = list(profile["requirements"])
        requirements += [
            "Representative domain dataset",
            "Evaluation metrics (accuracy, precision, recall, latency)",
            "MLOps / DevOps workflow (CI/CD, monitoring, retraining)",
        ]
        if regulatory_hits:
            for reg in regulatory_hits:
                requirements.append(f"Compliance: {reg.upper()}")
        requirements = list(dict.fromkeys(requirements))[:9]

        return {
            "field": field,
            "idea": idea,
            "rating": round(rating, 2),
            "verdict": self._verdict(rating),
            "difficulty": difficulty,
            "difficulty_color": diff_color,
            "scores": {
                "feasibility": round(feasibility, 1),
                "innovation": round(innovation, 1),
                "risk": round(risk, 1),
                "impact": round(impact, 1),
                "complexity": round(complexity, 1),
            },
            "pros": pros,
            "cons": cons,
            "key_challenges": challenges,
            "real_world_applications": applications,
            "components_required": components,
            "requirements": requirements,
            "suggested_tech_stack": suggested_stack,
            "market_opportunity": {
                "size": market_size,
                "note": market_note,
                "scale_detected": scale_label,
            },
            "estimated_budget_usd": round(total_budget, 0),
            "budget_breakdown_usd": budget_breakdown,
            "estimated_timeline_months": dev_months,
            "timeline_phases": phase_months,
            "note": "Budget and timeline are ML-assisted estimates. Actual costs vary by team, location, and scope.",
        }

    @staticmethod
    def _verdict(rating: float) -> str:
        if rating >= 8.5:
            return "Outstanding — pursue this idea"
        if rating >= 7.5:
            return "Excellent potential — strong foundation"
        if rating >= 6.5:
            return "Promising — worth building with refinements"
        if rating >= 5.5:
            return "Moderate potential — refine scope first"
        if rating >= 4.0:
            return "Risky — needs significant rethinking"
        return "High risk — major revision recommended"
