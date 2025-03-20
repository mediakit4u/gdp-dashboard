import streamlit as st

# Page configuration
st.set_page_config(page_title="Kevin Technologies", page_icon="☁️", layout="wide")

# Custom CSS for iPhone-style font and cloud boxes
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

        body {
            font-family: 'Inter', sans-serif;  /* iPhone-inspired font */
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        .main-title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: #00C3FF;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 22px;
            color: #FFFFFF; /* White text below the header */
            margin-bottom: 40px;
        }
        .cloud-box {
            width: 100%;
            text-align: center;
            padding: 20px;
            font-size: 18px;
            color: #00C3FF; /* Light blue text inside the cloud */
            background: transparent;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-weight: 600;
        }
        .cloud-shape {
            position: relative;
            width: 220px;
            height: 120px;
            background: #FFFFFF; /* White cloud box */
            border-radius: 50px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s, box-shadow 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-family: 'Inter', sans-serif; /* Ensuring SF Pro look */
        }
        .cloud-shape:before, .cloud-shape:after {
            content: '';
            position: absolute;
            background: #FFFFFF;
            border-radius: 50%;
        }
        .cloud-shape:before {
            width: 80px;
            height: 80px;
            top: -40px;
            left: 30px;
        }
        .cloud-shape:after {
            width: 100px;
            height: 100px;
            top: -50px;
            right: 30px;
        }
        .cloud-shape:hover {
            transform: scale(1.05);
            box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.3);
        }
        .service-text {
            color: #FFFFFF; /* White text below the cloud boxes */
            font-size: 16px;
            margin-top: 10px;
        }
        .footer {
            text-align: center;
            font-size: 16px;
            margin-top: 50px;
            color: #AAAAAA;
        }
        .contact-box {
            background: #333333;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            color: #FFFFFF;
            border: 1px solid #00C3FF;
            font-family: 'Inter', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="main-title">☁️ Kevin Technologies</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Empowering businesses with innovative digital solutions</p>', unsafe_allow_html=True)

# Services Section
st.write("### 🌟 Our Services")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="cloud-box">
        <div class="cloud-shape">🌍 Web Development</div>
        <p class="service-text">Custom, responsive, and high-performing websites.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="cloud-box">
        <div class="cloud-shape">📢 Digital Marketing</div>
        <p class="service-text">SEO, social media, and performance marketing solutions.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="cloud-box">
        <div class="cloud-shape">📈 Business Growth</div>
        <p class="service-text">Data-driven strategies to scale businesses.</p>
    </div>
    """, unsafe_allow_html=True)

# Contact Section
st.write("### 📞 Get in Touch")
st.markdown('<div class="contact-box">📩 Email: contact@kevintech.com <br> 🌐 Website: www.kevintech.com <br> 📞 Phone: +91 9876543210</div>', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">© 2025 Kevin Technologies. All Rights Reserved.</p>', unsafe_allow_html=True)


