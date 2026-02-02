import streamlit as st
import random

st.set_page_config(
    page_title="Will You Be My Valentine?",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #ffe0f0 25%, #ffd4e8 50%, #ffc8e0 75%, #ffbcd8 100%);
    }
    
    .main-title {
        font-size: 4rem;
        color: ##000000;
        text-align: center;
        font-family: 'Pacifico', cursive;
        margin-bottom: 2rem;
        animation: pulse 2s ease-in-out infinite;
    }
    
    
    .success-message {
        font-size: 3rem;
        color: #000000;
        text-align: center;
        font-family: 'Pacifico', cursive;
        animation: fadeIn 0.5s ease;
    }
    
    div.stButton > button {
        font-size: 1.5rem;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    #no-button-container {
        position: relative;
        transition: all 0.3s ease;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
</style>

<script>
window.addEventListener("load", () => {
    setTimeout(initNoButtonEscape, 800);
});

function initNoButtonEscape() {
    const doc = parent.document;

    function findNoButton() {
        return [...doc.querySelectorAll("button")]
            .find(b => b.innerText.trim().toLowerCase() === "no");
    }

    const noButton = findNoButton();
    if (!noButton) {
        setTimeout(initNoButtonEscape, 400);
        return;
    }

    const container = noButton.closest('div[data-testid="column"]');
    if (!container) return;

    noButton.style.pointerEvents = "none";
    noButton.style.cursor = "not-allowed";

    container.style.position = "fixed";
    container.style.zIndex = "9999";
    container.style.transition = "transform 0.05s linear";

    function teleport() {
        const pad = 100;
        const maxX = window.innerWidth - container.offsetWidth - pad;
        const maxY = window.innerHeight - container.offsetHeight - pad;

        const x = Math.random() * maxX;
        const y = Math.random() * maxY;

        container.style.left = `${x}px`;
        container.style.top = `${y}px`;
    }

    teleport();

    doc.addEventListener("mousemove", e => {
        const r = container.getBoundingClientRect();

        const cx = r.left + r.width / 2;
        const cy = r.top + r.height / 2;

        const dx = e.clientX - cx;
        const dy = e.clientY - cy;
        const dist = Math.hypot(dx, dy);

        if (dist < 300) {
            teleport();
        }
    });

    noButton.addEventListener("mouseenter", teleport);
}
</script>

""", unsafe_allow_html=True)

def click_yes():
    st.session_state.answered = True

def click_no():
    st.session_state.no_attempts += 1

if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'no_attempts' not in st.session_state:
    st.session_state.no_attempts = 0

if not st.session_state.answered:
    st.markdown('<h1 class="main-title">Will You Be My Valentine?????????????</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        yes = 1 + (st.session_state.no_attempts * 0.50)
        st.markdown(f"""
        <style>
            div.stButton > button:first-child {{
                background: linear-gradient(135deg, #ff1493, #ff69b4);
                color: white;
                transform: scale({yes});
                box-shadow: 0 6px 20px rgba(255, 20, 147, 0.4);
            }}
        </style>
        """, unsafe_allow_html=True)
        st.button("Mhm", on_click=click_yes, use_container_width=True, key="yes_button")
    
    if st.session_state.no_attempts > 0:
        positions = [col1, col2, col3]
        random_col = random.choice(positions)
        with random_col:
            st.button("M-m", on_click=click_no, use_container_width=True, key="no_button")
    else:
        with col1:
            st.button("M-m", on_click=click_no, use_container_width=True, key="no_button")
    
    if st.session_state.no_attempts > 0:
        st.markdown("---")
        messages = [
            "pleaseeeeeeeee",
            "I can do this all day",
            "Im just a baby",
            "Pretty please?????? with a cherry on top",
            "Do it for the dilfs, the daddy, the daddy version me",
            "BEBBEEEEEEE im not giving up"
        ]
        attempt_index = min(st.session_state.no_attempts - 1, len(messages) - 1)
        st.info(messages[attempt_index])

else:
    st.markdown('<h1 class="success-message">YAYAYAYAAYAYYY MWAHHHH YOURE MINE MWEHEHEHE...sorry i just got excited</h1>', unsafe_allow_html=True)
