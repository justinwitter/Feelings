import streamlit as st
import random
from typing import List, Dict

# Define balanced lists of feelings
POSITIVE_FEELINGS = [
    "Excited", "Happy", "Grateful", "Confident", "Energized", "Motivated",
    "Proud", "Accomplished", "Optimistic", "Peaceful", "Content", "Inspired",
    "Creative", "Attentive", "Determined", "Hopeful", "Joyful", "Satisfied",
    "Encouraged", "Empowered", "Refreshed", "Calm", "Enthusiastic", "Valued",
    "Appreciated", "Successful", "Fulfilled", "Radiant", "Curious", "Engaged",
    # Additional positive feelings
    "Elated", "Thrilled", "Delighted", "Cheerful", "Uplifted", "Invigorated",
    "Passionate", "Vibrant", "Ambitious", "Triumphant", "Blissful", "Ecstatic",
    "Exhilarated", "Glowing", "Jovial", "Lively", "Spirited", "Upbeat",
    "Zealous", "Dynamic", "Fantastic", "Gleeful", "Jubilant", "Magnificent",
    "Outstanding", "Spectacular", "Wonderful", "Amazing", "Brilliant", "Dazzling",
    # More positive feelings
    "Blessed", "Fortunate", "Lucky", "Privileged", "Honored", "Celebrated",
    "Cherished", "Adored", "Beloved", "Treasured", "Admired", "Respected",
    "Esteemed", "Revered", "Acclaimed", "Recognized", "Validated", "Affirmed",
    "Supported", "Nurtured", "Cared-for", "Protected", "Secure", "Safe",
    "Comfortable", "Cozy", "Warm", "Tender", "Compassionate", "Kind"
]


NEUTRAL_FEELINGS = [
    "Steady", "Equanimous", "Neutral", "Reflective", "Thoughtful", "Cautious",
    "Reserved", "Observant", "Contemplative", "Patient", "Measured", "Stable",
    "Composed", "Centered", "Relaxed", "Quiet", "Mellow", "Even-tempered",
    "Introspective", "Mindful", "Present", "Accepting", "Realistic", "Practical",
    # Additional neutral feelings
    "Consistent", "Levelheaded", "Rational", "Logical", "Reasonable", "Sensible",
    "Grounded", "Rooted", "Anchored", "Settled", "Established", "Fixed",
    "Unwavering", "Constant", "Unchanging", "Predictable", "Regular", "Routine",
    "Ordinary", "Normal", "Typical", "Average", "Standard", "Conventional",
    "Traditional", "Classic", "Timeless", "Enduring", "Lasting", "Permanent",
    # More neutral feelings
    "Detached", "Objective", "Impartial", "Unbiased", "Fair", "Just",
    "Equitable", "Moderate", "Temperate", "Mild", "Balanced", "Soft",
    "Subtle", "Understated", "Modest", "Humble", "Simple",
    "Plain", "Basic", "Fundamental", "Essential", "Core", "Central",
    "Concentrated", "Attuned", "Attentive-minded", "Alert", "Aware", "Conscious"
]


CHALLENGING_FEELINGS = [
    "Stressed", "Overwhelmed", "Tired", "Frustrated", "Anxious", "Uncertain",
    "Disappointed", "Concerned", "Worried", "Drained", "Pressured", "Confused",
    "Restless", "Impatient", "Discouraged", "Tense", "Stretched", "Challenged",
    "Conflicted", "Hesitant", "Unsettled", "Burdened", "Scattered", "Depleted",
    "Apprehensive", "Doubtful", "Weary", "Strained", "Irritated", "Fatigued",
    # Additional challenging feelings
    "Exhausted", "Burnt-out", "Swamped", "Frazzled", "Frantic", "Panicked",
    "Distressed", "Troubled", "Disturbed", "Agitated", "Flustered", "Rattled",
    "Shaken", "Startled", "Alarmed", "Dismayed", "Perturbed", "Vexed",
    "Annoyed", "Irked", "Bothered", "Aggravated", "Exasperated", "Fed-up",
    "Disheartened", "Dejected", "Downcast", "Gloomy", "Melancholy", "Somber",
    # More challenging feelings
    "Vulnerable", "Exposed", "Raw", "Sensitive", "Fragile", "Delicate",
    "Unstable", "Shaky", "Unsteady", "Wobbly", "Precarious", "Risky",
    "Dangerous", "Threatening", "Intimidating", "Scary", "Frightening", "Terrifying",
    "Horrifying", "Shocking", "Stunning", "Surprising", "Unexpected", "Unpredictable",
    "Chaotic", "Turbulent", "Stormy", "Tempestuous", "Wild", "Uncontrolled",
    "Reckless", "Impulsive", "Hasty", "Rushed", "Hurried", "Frenzied"
]


def generate_balanced_feelings(num_feelings: int) -> List[str]:
    """Generate a balanced mix of positive, neutral, and challenging feelings."""
    # Calculate distribution (roughly 40% positive, 30% neutral, 30% challenging)
    positive_count = max(1, int(num_feelings * 0.4))
    neutral_count = max(1, int(num_feelings * 0.3))
    challenging_count = num_feelings - positive_count - neutral_count
    
    # Sample from each category
    selected_positive = random.sample(POSITIVE_FEELINGS, min(positive_count, len(POSITIVE_FEELINGS)))
    selected_neutral = random.sample(NEUTRAL_FEELINGS, min(neutral_count, len(NEUTRAL_FEELINGS)))
    selected_challenging = random.sample(CHALLENGING_FEELINGS, min(challenging_count, len(CHALLENGING_FEELINGS)))
    
    # Combine and shuffle
    all_feelings = selected_positive + selected_neutral + selected_challenging
    random.shuffle(all_feelings)
    
    return all_feelings

def get_feeling_color(feeling: str) -> str:
    """Return CSS color based on feeling category."""
    if feeling in POSITIVE_FEELINGS:
        return "#e8f5e8"  # Light green
    elif feeling in NEUTRAL_FEELINGS:
        return "#f0f0f0"  # Light gray
    else:
        return "#fff2e8"  # Light orange

def main():
    st.set_page_config(
        page_title="Team Feelings Check-in",
        page_icon="😊",
        layout="wide"
    )
    
    st.title("🌟 Team Feelings Check-in")
    st.markdown("**Select the feeling that best describes how your week is going!**")
    
    # Initialize session state
    if 'feelings_list' not in st.session_state:
        st.session_state.feelings_list = generate_balanced_feelings(20)
    if 'selected_feelings' not in st.session_state:
        st.session_state.selected_feelings = set()
    if 'num_feelings' not in st.session_state:
        st.session_state.num_feelings = 20
    
    # Sidebar controls
    with st.sidebar:
        st.header("Settings")
        
        # Number of feelings slider
        new_num_feelings = st.slider(
            "Number of feelings to show:",
            min_value=5,
            max_value=50,
            value=st.session_state.num_feelings,
            step=1
        )
        
        # Regenerate if number changed
        if new_num_feelings != st.session_state.num_feelings:
            st.session_state.num_feelings = new_num_feelings
            st.session_state.feelings_list = generate_balanced_feelings(new_num_feelings)
            st.session_state.selected_feelings = set()
        
        # Regenerate button
        if st.button("🔄 Generate New Feelings", use_container_width=True):
            st.session_state.feelings_list = generate_balanced_feelings(st.session_state.num_feelings)
            st.session_state.selected_feelings = set()
            st.rerun()
        
        # Clear selections button
        if st.button("🗑️ Clear All Selections", use_container_width=True):
            st.session_state.selected_feelings = set()
            st.rerun()
        
        # Show legend
        st.markdown("---")
        st.markdown("**Legend:**")
        st.markdown("🟢 **Positive feelings**")
        st.markdown("⚪ **Neutral feelings**") 
        st.markdown("🟡 **Challenging feelings**")
        
        # Show selection count
        if st.session_state.selected_feelings:
            st.markdown("---")
            st.markdown(f"**Selected: {len(st.session_state.selected_feelings)} feelings**")
            for feeling in sorted(st.session_state.selected_feelings):
                st.markdown(f"• {feeling}")
    
    # Main grid area
    st.markdown("### Click on feelings as team members choose them:")
    
    # Calculate grid dimensions
    num_feelings = len(st.session_state.feelings_list)
    cols_per_row = min(5, num_feelings)  # Max 5 columns
    
    # Create CSS for custom button styling
    st.markdown("""
    <style>
    div[data-testid="stButton"] > button {
        transition: all 0.3s ease;
    }
    
    /* Selected button styling */
    .selected-feeling {
        background-color: #dc3545 !important;
        color: white !important;
        border: 3px solid #721c24 !important;
        box-shadow: 0 4px 12px rgba(220, 53, 69, 0.4) !important;
        transform: translateY(-2px);
        font-weight: bold !important;
    }
    
    .selected-feeling:hover {
        background-color: #c82333 !important;
        border-color: #5a171e !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display feelings in a grid
    for i in range(0, num_feelings, cols_per_row):
        cols = st.columns(cols_per_row)
        
        for j in range(cols_per_row):
            if i + j < num_feelings:
                feeling = st.session_state.feelings_list[i + j]
                
                with cols[j]:
                    # Determine if feeling is selected
                    is_selected = feeling in st.session_state.selected_feelings
                    
                    # Display the feeling
                    display_text = f"✅ {feeling}" if is_selected else feeling
                    
                    # Use button to toggle selection
                    if st.button(
                        display_text,
                        key=f"feeling_{i+j}_{feeling}",
                        use_container_width=True,
                        type="primary" if is_selected else "secondary",
                        help=f"Click to {'deselect' if is_selected else 'select'} {feeling}"
                    ):
                        if feeling in st.session_state.selected_feelings:
                            st.session_state.selected_feelings.remove(feeling)
                        else:
                            st.session_state.selected_feelings.add(feeling)
                        st.rerun()
    
    # Summary and Team Mood Analysis
    if st.session_state.selected_feelings:
        st.markdown("---")
        
        # Calculate mood distribution
        positive_count = sum(1 for f in st.session_state.selected_feelings if f in POSITIVE_FEELINGS)
        neutral_count = sum(1 for f in st.session_state.selected_feelings if f in NEUTRAL_FEELINGS)
        challenging_count = sum(1 for f in st.session_state.selected_feelings if f in CHALLENGING_FEELINGS)
        total_selected = len(st.session_state.selected_feelings)
        
        # Team mood analysis
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### 📊 Team Mood Overview")
            
            # Calculate percentages
            pos_pct = (positive_count / total_selected * 100) if total_selected > 0 else 0
            neu_pct = (neutral_count / total_selected * 100) if total_selected > 0 else 0
            cha_pct = (challenging_count / total_selected * 100) if total_selected > 0 else 0
            
            # Display metrics
            st.metric("🟢 Positive", f"{positive_count}")
            st.metric("⚪ Neutral", f"{neutral_count}")
            st.metric("🟡 Challenging", f"{challenging_count}")
        
        with col2:
            st.markdown("### 💭 Team Sentiment Analysis")
            
            # Provide insights based on the distribution
            if pos_pct >= 60:
                st.success("🌟 **High energy week!** Lots of positive vibes flowing through the team.")
            elif pos_pct >= 40:
                st.info("😊 **Balanced energy.** The team is experiencing a nice mix of feelings this week.")
            elif cha_pct >= 60:
                st.warning("🤗 **Intense week.** The team is navigating some challenging waters together.")
            else:
                st.info("🤔 **Varied experiences.** Team members are having quite different weeks.")
            
            # Show total participation without pressure
            if total_selected >= 3:
                st.success(f"👥 {total_selected} team members sharing their week!")
        
        st.markdown("---")
        st.success(f"**{total_selected} team member(s) have shared their feelings:**")
        
        # Display selected feelings in a nice format grouped by category
        if positive_count > 0:
            st.markdown("**🟢 Positive feelings:**")
            positive_feelings = [f for f in st.session_state.selected_feelings if f in POSITIVE_FEELINGS]
            st.write(", ".join(sorted(positive_feelings)))
        
        if neutral_count > 0:
            st.markdown("**⚪ Neutral feelings:**")
            neutral_feelings = [f for f in st.session_state.selected_feelings if f in NEUTRAL_FEELINGS]
            st.write(", ".join(sorted(neutral_feelings)))
        
        if challenging_count > 0:
            st.markdown("**🟡 Challenging feelings:**")
            challenging_feelings = [f for f in st.session_state.selected_feelings if f in CHALLENGING_FEELINGS]
            st.write(", ".join(sorted(challenging_feelings)))

if __name__ == "__main__":
    main()
