import streamlit as st
from quantum import get_password_by_strength, QuantumAPIError

# Load external CSS
def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Quantum Random Password Generator", page_icon="🔐", layout="centered")

    # Load your custom CSS
    load_css("static/cyberpunk.css")

    st.title("🔐 Quantum Random Password Generator")
    st.markdown("Protect your identity with **true quantum randomness** ✨")

    strength = st.selectbox("Select Password Strength:", ["Weak", "Medium", "Strong"])

    if st.button("⚡ Generate Password"):
        with st.spinner("Generating password with quantum entropy..."):
            try:
                password = get_password_by_strength(strength)
                st.markdown("### ✅ Your Quantum Password:")
                st.code(password, language='plaintext')
            except QuantumAPIError as e:
                st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
