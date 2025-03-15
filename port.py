import streamlit as st

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Contact"])

# Home Section
if page == "Home":
    st.title("Welcome to My Portfolio! 👋")
    st.image(r"c:\Users\kdeepak_new\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\TempState\04025959B191F8F9DE3F924F0940515F\WhatsApp Image 2025-03-14 at 23.54.17_70b3a793.jpg", width=200)
    st.write("Hi, I'm Deepak, a passionate Data Scientist & Machine Learning Engineer.")
    st.write("I love working with AI, NLP, and Deep Learning to solve real-world problems.")

# Projects Section
elif page == "Projects":
    st.title("My Projects 🚀")
    st.write("### 1. Medical Chatbot")
    st.write("- An AI-powered Medical Chatbot that provides accurate healthcare responses by extracting medical knowledge")
    st.write("- Tools: Python, GeminiAI, Pinecone")
    st.write("[GitHub Repo](https://github.com/Deepak-Rauta/Medico_Chatbot.git)")
    
    st.write("### 2. Vehicle Number Plate Detection")
    st.write("- A Streamlit-based Vehicle Number Plate Detection app that uses OpenCV and Tesseract OCR to detect and extract text from number plates in uploaded images.")
    st.write("- Tools: Python, OpenCV, EasyOCR, Streamlit")
    st.write("[GitHub Repo](https://github.com/Deepak-Rauta/Numberplate-Detection-using-openCV-and-easy-OCR.git)")

# Skills Section
elif page == "Skills":
    st.title("My Skills & Tech Stack 💡")
    st.write("**Programming:** Python, SQL, R")
    st.write("**Data Science:** Pandas, NumPy, Scikit-Learn, TensorFlow, PyTorch")
    st.write("**Visualization:** Power BI, Matplotlib, Seaborn")
    st.write("**Cloud & Deployment:** AWS, GitHub, Streamlit Share")

# Contact Section
elif page == "Contact":
    st.title("Let's Connect! 📩")
    st.write("📧 Email: kdeepak8250@gmail.com")
    st.write("🔗 LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/deepak-rauta/)")
    st.write("🐙 GitHub: [github.com/yourgithub](https://github.com/Deepak-Rauta)")

# Deployment Tip: Use 'streamlit static' or 'GitHub Actions' for GitHub Pages
