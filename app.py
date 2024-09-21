import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Enhanced Leaf Analysis",
    page_icon="🍃",
    layout="wide"
)

# Custom CSS for dark teal background, white text, and enhanced styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0a4d4d;
        background-image: 
            radial-gradient(circle at 100% 150%, #0a4d4d 24%, #0c5c5c 25%, #0c5c5c 28%, #0a4d4d 29%, #0a4d4d 36%, #0c5c5c 36%, #0c5c5c 40%, transparent 40%, transparent),
            radial-gradient(circle at 0 150%, #0a4d4d 24%, #0c5c5c 25%, #0c5c5c 28%, #0a4d4d 29%, #0a4d4d 36%, #0c5c5c 36%, #0c5c5c 40%, transparent 40%, transparent),
            radial-gradient(circle at 50% 100%, #0c5c5c 10%, #0a4d4d 11%, #0a4d4d 23%, #0c5c5c 24%, #0c5c5c 30%, #0a4d4d 31%, #0a4d4d 43%, #0c5c5c 44%, #0c5c5c 50%, #0a4d4d 51%, #0a4d4d 63%, #0c5c5c 64%, #0c5c5c 71%, transparent 71%, transparent),
            radial-gradient(circle at 100% 50%, #0c5c5c 5%, #0a4d4d 6%, #0a4d4d 15%, #0c5c5c 16%, #0c5c5c 20%, #0a4d4d 21%, #0a4d4d 30%, #0c5c5c 31%, #0c5c5c 35%, #0a4d4d 36%, #0a4d4d 45%, #0c5c5c 46%, #0c5c5c 49%, transparent 50%, transparent),
            radial-gradient(circle at 0 50%, #0c5c5c 5%, #0a4d4d 6%, #0a4d4d 15%, #0c5c5c 16%, #0c5c5c 20%, #0a4d4d 21%, #0a4d4d 30%, #0c5c5c 31%, #0c5c5c 35%, #0a4d4d 36%, #0a4d4d 45%, #0c5c5c 46%, #0c5c5c 49%, transparent 50%, transparent);
        background-size: 100px 50px;
        color: white;
    }
    .stSelectbox [data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    .stSelectbox [data-baseweb="select"] > div {
        color: white !important;
    }
    .custom-container {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        backdrop-filter: blur(5px);
    }
    .custom-title {
        color: #a7d7c5;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .custom-subtitle {
        color: #f0f4c3;
        font-size: 24px;
        text-align: center;
        margin-bottom: 30px;
        font-style: italic;
    }
    .custom-text {
        font-size: 18px;
        line-height: 1.6;
    }
    .custom-button {
        background-color: #74b49b;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        font-size: 18px;
        transition: all 0.3s ease;
    }
    .custom-button:hover {
        background-color: #5c9b84;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stProgress > div > div > div > div {
        background-color: #74b49b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.markdown('<h2 style="color: #a7d7c5;">Leaf Detection Options</h2>', unsafe_allow_html=True)

# Dropdown for leaf type
leaf_type = st.sidebar.selectbox(
    "Select Leaf Type",
    ["Apple","Corn","Potato","Tomato"]
)

# Dropdown for season
season = st.sidebar.selectbox(
    "Select Season",
    ["Spring", "Summer", "Fall", "Winter"]
)

# Checkbox for advanced options
advanced_options = st.sidebar.checkbox("Show Advanced Options")

if advanced_options:
    detection_mode = st.sidebar.radio(
        "Detection Mode",
        ["Fast", "Balanced", "Accurate"]
    )
    
    leaf_condition = st.sidebar.multiselect(
        "Leaf Condition",
        ["Healthy", "Diseased", "Pest-infested", "Drought-stressed"]
    )

# Main content
st.markdown('<h1 class="custom-title">🍃 Leaf Detection Interface</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="custom-subtitle">Unveiling Nature\'s Intricate Patterns</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="custom-container custom-text">
    Welcome to our refined Enhanced Leaf Analysis App. Immerse yourself in the subtle complexities of botanical analysis. 
    Our state-of-the-art model is crafted to identify and examine diverse leaf types across the seasons, 
    offering you a nuanced understanding of nature's artistry.
    
    <h3 style="color: #f0f4c3; margin-top: 20px;">Embark on Your Botanical Journey:</h3>
    <ol>
        <li>Choose your anticipated leaf type from the sidebar options.</li>
        <li>Select the current season for a contextually rich analysis.</li>
        <li>Upload a high-quality image of the leaf you wish to explore.</li>
        <li>Initiate the analysis to uncover the leaf's hidden characteristics.</li>
    </ol>
    </div>
    """,
    unsafe_allow_html=True
)

# File uploader
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Analyze Leaf", key="analyze_button"):
        # Simulating analysis process
        st.write("Analyzing...")
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
        
        # Simulated results
        detected_type = leaf_type if random.random() > 0.3 else random.choice(["Apple","Corn","Potato","Tomato"])
        
        st.success("Analysis Complete")
        st.markdown(f'<div class="custom-container"><h3 style="color: #f0f4c3;">Analysis Results:</h3>', unsafe_allow_html=True)
        st.write(f"Detected Leaf Type: {detected_type}")
        st.write(f"Analyzed for {season} season")
        
        # Additional information based on season
        st.subheader("Leaf Characteristics")
        seasonal_info = {
            "Spring": "Emerging growth, vibrant green hues",
            "Summer": "Mature foliage, deep green tones",
            "Fall": "Transitional colors, preparing for senescence",
            "Winter": "Dormant phase or persistent evergreen (for conifers)"
        }
        
        st.markdown(
            f"""
            <div class="custom-text">
            The {detected_type} leaf in {season}:
            <ul>
                <li>Seasonal Trait: {seasonal_info[season]}</li>
                <li>Morphology: {random.choice(['Lobed', 'Ovate', 'Acicular', 'Cordate'])}</li>
                <li>Margin: {random.choice(['Serrate', 'Entire', 'Undulate'])}</li>
                <li>Texture: {random.choice(['Glabrous', 'Pubescent', 'Coriaceous'])}</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if advanced_options and leaf_condition:
            st.subheader("Leaf Health Assessment")
            health_analysis = "<ul>"
            for condition in leaf_condition:
                if random.choice([True, False]):
                    health_analysis += f"<li>{condition}: Detected"
                    if condition == "Diseased":
                        health_analysis += f" - Potential pathogen: {random.choice(['Anthracnose', 'Powdery Mildew', 'Leaf Rust'])}"
                    elif condition == "Pest-infested":
                        health_analysis += f" - Possible pest: {random.choice(['Aphids', 'Leaf Miners', 'Scale Insects'])}"
                    health_analysis += "</li>"
                else:
                    health_analysis += f"<li>{condition}: Not detected</li>"
            health_analysis += "</ul>"
            st.markdown(f'<div class="custom-text">{health_analysis}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Add a decorative element at the bottom
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <svg width="200" height="50">
            <path d="M10 25 Q 50 10, 100 25 T 190 25" stroke="#a7d7c5" stroke-width="3" fill="none" />
            <circle cx="10" cy="25" r="4" fill="#f0f4c3" />
            <circle cx="100" cy="25" r="4" fill="#f0f4c3" />
            <circle cx="190" cy="25" r="4" fill="#f0f4c3" />
        </svg>
    </div>
    """,
    unsafe_allow_html=True
)