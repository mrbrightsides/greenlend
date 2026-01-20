import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Green Lend",
    page_icon="💵",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/Rd8GyFU.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **Green Lend** empowers underserved communities with AI-powered sustainable microfinance solutions.
    
    ---
    
    #### 🔮 Vision Statement
    
    We envision a world where microfinance is not just about providing loans, but about fostering sustainable development and positive environmental impact through every transaction.

    > The original version can be accessed here https://greenlend.elpeef.com/
   
    ---
   
    ### 🧩 Apps Showcase
    Our other apps and tools can be seen here:
    [ELPEEF](https://showcase.elpeef.com/)
    
    ---
  
    #### 🙌 Support & Contribute
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/greenlend)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

def embed_iframe(src, height=900):
    components.html(f"""
    <div style="width:100%; height:{height}px;">
        <iframe src="{src}"
                style="width:100%; height:100%; border:none; border-radius:12px;">
        </iframe>
    </div>
    """, height=height)

iframe_url = "https://greenlend.elpeef.com/"

embed_iframe(iframe_url, height=900)
