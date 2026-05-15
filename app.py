import streamlit as st
import yfinance as yf
import base64
from pathlib import Path

IDX_LOGO_PATH = "C:/Users/j450n/Downloads/1752803497-6879a8a90429c.webp"
LINKEDIN_LOGO_PATH = "C:/Users/j450n/Downloads/LinkedIn_logo_initials.png"
GITHUB_LOGO_PATH = "C:/Users/j450n/Downloads/github-6980894_1280.png"
BG_IMAGE_PATH = "C:/Users/j450n/Downloads/jakub-zerdzicki-ip7GFn5JqX8-unsplash.jpg"

st.markdown(
    """
    <style>
    .stTextInput > div > input:hover, .stNumberInput > div > input:hover {
        border-color: #31D957 !important;
        box-shadow: 0 0 0 2px #32c25244 !important;
    }
    div[data-baseweb="input"] > div > input:hover {
        border-color: #31D957 !important;
        box-shadow: 0 0 0 2px #32c25244 !important;
    }
    .stNumberInput button:hover {
        border-color: #31D957 !important;
        box-shadow: 0 0 0 2px #32c25244 !important;
    }
    .stTextInput > div > input:focus, .stNumberInput > div > input:focus {
        border-color: #31D957 !important;
        box-shadow: 0 0 0 3px #32c25291 !important;
    }
    div[data-baseweb="input"] > div > input:focus {
        border-color: #31D957 !important;
        box-shadow: 0 0 0 2px #32c25244 !important;
    }
    .stTextInput > div > input, .stNumberInput > div > input {
        transition: border-color 0.16s, box-shadow 0.16s;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

bg_base64 = image_to_base64(BG_IMAGE_PATH)
idx_logo_base64 = image_to_base64(IDX_LOGO_PATH)
linkedin_logo_base64 = image_to_base64(LINKEDIN_LOGO_PATH)
github_logo_base64 = image_to_base64(GITHUB_LOGO_PATH)

st.set_page_config(
    page_title="Dividend Compass",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="auto"
)

st.session_state.theme_mode = "Dark"

def css_for_theme(mode):
    return f"""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
    body, .stApp {{
        background-image: url('data:image/jpeg;base64,{bg_base64}');
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }}
    .block-container {{
        padding-top: 1.3rem;
        padding-bottom: 1.5rem;
        background-color: rgba(26,27,36,0.90);
        border-radius: 18px;
        max-width: 430px;
        margin: 40px auto 0 auto;
        border: 1px solid #34374c;
        backdrop-filter: blur(8px);
        box-shadow: 0 4px 32px rgba(34, 36, 55, 0.32);
    }}
    * {{
        font-family: 'Poppins', Arial, Helvetica, sans-serif !important;
    }}
    h1, h3, p, label {{
        color: #EEE !important;
        font-family: 'Poppins', Arial, Helvetica, sans-serif !important;
        text-align: center;
        margin-top: 0.3em !important;
        margin-bottom: 0.3em !important;
    }}
    /* The line below hid the Streamlit toolbar. We REMOVE IT so Streamlit toolbar is visible, by commenting it out: */
    /* #MainMenu, header, footer {{
        visibility: hidden;
        height: 0;
    }} */
    .metric-card {{
        background: linear-gradient(120deg,#232a31 92%,#135036 100%);
        border-radius: 17px;
        border: 1.2px solid #34374c;
        box-shadow: 0 2px 18px 0 rgba(32,41,21,0.12), 0 1.5px 0px 0 rgba(90,169,90,0.09);
        padding: 1em 1em 1em 1em;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 1.2em;
    }}
    .metric-amount {{
        color: #51ca7c;
        font-size: 2.04em;
        font-weight: 500;
        letter-spacing: .5px;
        margin-bottom: 0.07em;
        font-family: 'Poppins', Arial, Helvetica, sans-serif !important;
    }}
    .metric-caption {{
        color: #c4c7de;
        font-size: 0.98em;
        text-align: center;
        margin-top: 0.1em;
        margin-bottom: -0.25em;
        font-family: 'Poppins', Arial, Helvetica, sans-serif !important;
    }}
    .muted {{
        color: #7d8199 !important;
        font-size: .982em !important;
        font-family: 'Poppins', Arial, Helvetica, sans-serif !important;
    }}
    .idx-logo {{
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 1.1rem;
        margin-top: 0.5rem;
        width: 98px;
        height: auto;
        filter: drop-shadow(0px 4px 16px rgba(15,32,75,0.16));
        border-radius: 14px;
        background: rgba(24,24,26,0.25);
    }}
    .stTextInput > div > input:hover, .stNumberInput > div > input:hover {{
        border-color: #31D957 !important;
        box-shadow: 0 0 0 2px #32c25244 !important;
    }}
    div[data-baseweb="input"] > div > input:hover {{
        border-color: #31D957 !important;
        box-shadow: 0 0 0 2px #32c25244 !important;
    }}
    .stNumberInput button:hover {{
        border-color: #31D957 !important;
        box-shadow: 0 0 0 2px #32c25244 !important;
    }}
    .stTextInput > div > input:focus, .stNumberInput > div > input:focus {{
        border-color: #31D957 !important;
        box-shadow: 0 0 0 3px #32c25291 !important;
    }}
    div[data-baseweb="input"] > div > input:focus {{
        border-color: #31D957 !important;
        box-shadow: 0 0 0 2px #32c25244 !important;
    }}
    .stTextInput > div > input, .stNumberInput > div > input {{
        transition: border-color 0.16s, box-shadow 0.16s;
    }}
    .custom-footer {{
        text-align: center;
        margin-top: 2.1em;
        color: #ccc;
        font-size: 0.92em;
        padding-bottom: 2em;
        opacity: 0.96;
    }}
    .footer-links {{
        margin-top: 0.51em;
        display: flex;
        flex-direction: row;
        gap: 9px;
        justify-content: center;
    }}
    .footer-link-btn {{
        display: flex;
        align-items: center;
        gap: 0.45em;
        padding: 0.13em 0.67em;
        font-size: 0.92em;
        border-radius: 12px;
        border: none;
        font-family: 'Poppins', Arial, Helvetica, sans-serif !important;
        font-weight: 500;
        text-decoration: none;
        color: #fff !important;
        background-color: #126bc4 !important;
        margin-right: 0.26em;
        transition: background .14s, color .14s;
        box-shadow: 0 1px 3px rgba(44,108,231,0.10);
        position: relative;
        min-width: 68px;
        max-height: 32px;
        justify-content: center;
        line-height: 1;
    }}
    .footer-link-btn:last-child {{
        margin-right: 0;
        background: #222 !important;
    }}
    .footer-link-btn:hover {{
        filter: brightness(1.10) contrast(1.07);
        background: #2b8ce9 !important;
        color: #fff;
    }}
    .footer-link-btn.github:hover {{
        background: #252525 !important;
    }}
    .footer-link-icon {{
        height: 22px;
        width: 22px;
        min-width: 22px;
        min-height: 22px;
        border-radius: 4px;
        background: none;
        display: inline-block;
        vertical-align: bottom;
        margin-right: 0.13em;
    }}
    button[data-testid="baseButton-secondary"], div.stButton>button {{
      color: #fff !important;
    }}
    .milestone-heading {{
      color: #f1f1fa !important;
      font-family: 'Poppins', Arial, Helvetica, sans-serif !important;
      font-size: 1.09em !important;
      font-weight: 400 !important;
      text-align: center !important;
      letter-spacing: 0.01em;
      margin: 0.9em 0 0.1em 0;
      opacity: 0.93;
      font-style: italic;
      background: none;
    }}
    .milestone-separator {{
      width: 54%;
      max-width: 180px;
      margin: 0.5em auto 1.2em auto;
      border-bottom: 1.5px solid #353951;
      opacity: 0.63;
      border-radius: 2px;
      background: none;
    }}
    </style>
    """

st.markdown(css_for_theme("Dark"), unsafe_allow_html=True)

st.markdown(
    f"""
    <img src="data:image/webp;base64,{idx_logo_base64}" class="idx-logo"/>
    """,
    unsafe_allow_html=True
)

# Title only, link button beside the title removed
st.markdown(
    "<h1 style='text-align: center; margin-bottom: 0.3em; margin-top: 0.3em; color: #EEE; font-family: Poppins, Arial, Helvetica, sans-serif;'>Dividend <span style=\"display: inline-block; margin-left: 0.32em;\">Compass</span></h1>",
    unsafe_allow_html=True
)

with st.form(key="main_form", clear_on_submit=False):
    ticker = st.text_input("IDX Stock Code", placeholder="e.g. BBCA")
    lots = st.number_input("Number of Lots", min_value=1, step=1, value=1)
    submitted = st.form_submit_button("Calculate", use_container_width=True)

st.markdown("", unsafe_allow_html=True)

def format_rp(amount):
    s = f"{int(round(amount)):,}".replace(",", ".")
    return f"Rp {s}"

def format_dps_id(dps):
    return f"{int(round(dps)):,}".replace(",", ".")

milestones = {
    "Specialty Coffee": 50000,
    "Apple Music + iCloud": 65000,
    "Gym Membership": 350000,
}
milestone_icons = {
    "Specialty Coffee": "☕",
    "Apple Music + iCloud": "🎵",
    "Gym Membership": "🏋️",
}
milestone_keys = list(milestones.keys())

if submitted:
    if not ticker.strip():
        st.error("Please enter a valid IDX stock ticker.")
    else:
        with st.spinner("Fetching dividend info..."):
            try:
                full_ticker = ticker.strip().upper() + ".JK"
                stock = yf.Ticker(full_ticker)
                info = stock.info

                dividend_rate = info.get("dividendRate", None)
                price = info.get("regularMarketPrice", None)
                dividend_yield = info.get("trailingAnnualDividendYield", None)

                if isinstance(dividend_rate, (int, float)) and dividend_rate > 0:
                    annual_dividend_per_share = dividend_rate
                elif (
                    dividend_yield is not None 
                    and isinstance(dividend_yield, (int, float)) and dividend_yield > 0
                    and price is not None and isinstance(price, (int, float)) and price > 0
                ):
                    annual_dividend_per_share = price * dividend_yield
                else:
                    annual_dividend_per_share = None

                if annual_dividend_per_share is None or annual_dividend_per_share <= 0:
                    st.error(
                        "No valid dividend data found for this ticker, or the ticker is invalid. "
                        "Please check the IDX stock code (e.g., BBCA)."
                    )
                    st.session_state.total_net = None
                else:
                    total_gross = lots * 100 * annual_dividend_per_share
                    total_net = round(total_gross * 0.9)

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-amount">{format_rp(total_net)}</div>
                            <div class="metric-caption">Estimated Net Annual Dividend</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.markdown("<div class='milestone-separator'></div>", unsafe_allow_html=True)
                    st.markdown(
                        "<div class='milestone-heading'>Lifestyle Milestones</div>",
                        unsafe_allow_html=True
                    )

                    st.session_state.total_net = total_net

            except Exception as e:
                st.error("No dividend data found or unable to fetch data for this ticker. Please check the stock code and try again.")
                st.session_state.total_net = None
else:
    total_net = st.session_state.get("total_net", None)
    if total_net is not None:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-amount">{format_rp(total_net)}</div>
                <div class="metric-caption">Estimated Net Annual Dividend</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<div class='milestone-separator'></div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='milestone-heading'>Lifestyle Milestones</div>",
            unsafe_allow_html=True
        )

total_net = st.session_state.get("total_net", None)
if total_net is not None:
    milestone_selected = st.selectbox(
        "Choose a Milestone:",
        options=milestone_keys,
        format_func=lambda k: f"{milestone_icons[k]} {k} ({format_rp(milestones[k])})",
        key="milestone_selectbox"
    )

    units = int(total_net // milestones[milestone_selected])
    if units > 0:
        if milestone_selected in ["Apple Music + iCloud", "Gym Membership"]:
            score_text = (
                f"{milestone_icons[milestone_selected]} <b>Your dividends fund {units} months of {milestone_selected}!</b>"
            )
        else:
            score_text = (
                f"{milestone_icons[milestone_selected]} <b>Your dividends fund {units} cups of Specialty Coffee!</b>"
            )
        st.markdown(
            f"<div style='text-align:center; font-size:1.16em; margin-top:1em; color:#65e365;'>{score_text}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div class='muted' style='text-align:center; font-size:1.01em; margin-top:0.7em;'>Your dividends aren't enough to afford a {milestone_selected} yet.<br>Keep growing!</div>",
            unsafe_allow_html=True,
        )

st.markdown(
    f"""
    <div class="custom-footer">
        <div>
            <span style="font-size:0.97em;color:#eee;">Made by Jason Chandra</span>
        </div>
        <div class="footer-links">
            <a class="footer-link-btn" href="https://www.linkedin.com/in/jason-chandra-123264264/" target="_blank">
                <img src="data:image/png;base64,{linkedin_logo_base64}" class="footer-link-icon"/>
                LinkedIn
            </a>
            <a class="footer-link-btn github" href="https://github.com/jasonchndra" target="_blank">
                <img src="data:image/png;base64,{github_logo_base64}" class="footer-link-icon"/>
                GitHub
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)