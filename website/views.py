
from django.shortcuts import render
from django.http import Http404

SESSIONS = {
    "artificial-intelligence": {
        "title": "Artificial Intelligence",
        "icon": "🧠",
        "subtitle": "Explore the World of AI",
        "overview": (
            "Artificial Intelligence enables computers to perform "
            "tasks that usually require human intelligence, such as "
            "learning, reasoning, understanding language, and recognizing images."
        ),
        "topics": [
            "Introduction to Artificial Intelligence",
            "Types of AI: Narrow AI, General AI, and Super AI",
            "Machine Learning and Deep Learning",
            "Natural Language Processing (NLP)",
            "Computer Vision",
            "Generative AI and AI chatbots",
            "AI applications in education, healthcare, and agriculture",
            "Responsible and ethical use of AI",
        ],
        "activities": [
            "Explore AI tools and chatbots",
            "Build an image classifier using Teachable Machine",
            "Create a simple AI-based project",
        ],
        "applications": [
            "Voice assistants and speech recognition",
            "Personalized learning",
            "Medical image analysis",
            "Crop monitoring",
        ],
        "project": "AI-Based Smart Assistant",
    },

    "robotics": {
        "title": "Robotics and Electronics",
        "icon": "🤖",
        "subtitle": "Build, Program and Innovate",
        "overview": (
            "Robotics combines mechanical systems, electronics, "
            "sensors, and programming to create machines that perform tasks."
        ),
        "topics": [
            "Introduction to robotics",
            "Electronic components and circuits",
            "LEDs, buzzers, and resistors",
            "Sensors and actuators",
            "Arduino UNO",
            "Robot programming",
        ],
        "activities": [
            "Build an LED circuit",
            "Experiment with sensors",
            "Create an Arduino traffic light",
        ],
        "applications": [
            "Manufacturing",
            "Healthcare",
            "Space exploration",
            "Education",
        ],
        "project": "Arduino Smart Traffic Light",
    },

    "drone-technology": {
        "title": "Drone Technology",
        "icon": "🚁",
        "subtitle": "Discover the Technology of Flight",
        "overview": (
            "A drone is an aircraft that operates without a pilot "
            "on board. Drones may be remotely controlled or programmed "
            "to perform specific tasks. They use motors, propellers, "
            "sensors, batteries, and flight controllers."
        ),
        "topics": [
            "What is a drone?",
            "Types of drones",
            "Drone frame and propellers",
            "Motors, battery, and flight controller",
            "How drones take off, hover, and land",
            "Sensors and navigation",
            "Drone safety and responsible operation",
        ],
        "activities": [
            "Identify the components of a drone",
            "Learn how propellers help drones fly",
            "Explore drone flight principles",
            "Prepare a poster about drone applications",
        ],
        "applications": [
            "Agriculture and crop monitoring",
            "Aerial photography",
            "Disaster management and rescue",
            "Environmental monitoring",
            "Mapping and surveying",
        ],
        "project": "Smart Drone Applications",
    },

    "3d-printing": {
        "title": "3D Printing",
        "icon": "🖨️",
        "subtitle": "Turn Digital Ideas into Real Objects",
        "overview": (
            "3D printing creates physical objects from digital "
            "designs by building them layer by layer."
        ),
        "topics": [
            "Introduction to 3D printing",
            "3D design and modelling",
            "Digital models and slicing",
            "How a 3D printer works",
            "Printing materials",
            "Applications of 3D printing",
        ],
        "activities": [
            "Explore 3D models",
            "Design a simple object",
            "Learn the steps of 3D printing",
        ],
        "applications": [
            "Product design",
            "Education",
            "Healthcare",
            "Engineering",
        ],
        "project": "3D-Printed Nameplate",
    },

    "virtual-reality": {
        "title": "Virtual Reality",
        "icon": "🥽",
        "subtitle": "Explore Immersive Digital Worlds",
        "overview": (
            "Virtual Reality creates computer-generated environments "
            "that users can experience and explore using suitable devices."
        ),
        "topics": [
            "Introduction to Virtual Reality",
            "VR headsets and controllers",
            "Virtual environments",
            "VR in education",
            "VR in healthcare and entertainment",
            "Responsible use of VR",
        ],
        "activities": [
            "Explore virtual environments",
            "Learn how VR headsets work",
            "Discover educational VR applications",
        ],
        "applications": [
            "Virtual science laboratories",
            "Healthcare training",
            "Architecture and design",
            "Entertainment and games",
        ],
        "project": "Virtual Science Learning Experience",
    },
}


def home(request):
    return render(request, "website/home.html")


def session_detail(request, slug):
    session = SESSIONS.get(slug)

    if session is None:
        raise Http404("Session not found")

    return render(
        request,
        "website/session_detail.html",
        {"session": session},
    )
