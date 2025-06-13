# Cryptocurrency Advisor Chatbot - Rule-Based + Sustainability Analysis
# Theme: "Your First AI-Powered Financial Sidekick!" 

# Predefined Dataset (2025-06-13 Snapshot)
crypto_data = {
    "Bitcoin": {
        "price_trend": "volatile",  # Options: rising/falling/stable/volatile
        "energy_use": "high",       # Proof-of-Work (PoW)
        "project_activity": "high", # Developer engagement
        "risk_score": 7             # 1-10 (10=riskiest)
    },
    "Ethereum": {
        "price_trend": "rising",
        "energy_use": "medium",     # Proof-of-Stake (PoS)
        "project_activity": "high",
        "risk_score": 5
    },
    "Solana": {
        "price_trend": "stable",
        "energy_use": "low",
        "project_activity": "medium",
        "risk_score": 4
    },
    "Cardano": {
        "price_trend": "rising",
        "energy_use": "low",
        "project_activity": "high",
        "risk_score": 3
    }
}

# Core Advice Logic
def get_advice(coin_name):
    coin = crypto_data.get(coin_name.title())  # Handles case sensitivity
    if not coin:
        return "⚠️ I only analyze: Bitcoin, Ethereum, Solana, Cardano"
    
    # Profitability Rules
    if coin["price_trend"] == "rising":
        profit_advice = "💰 BUY opportunity (positive momentum)"
    elif coin["price_trend"] == "falling":
        profit_advice = "🔻 CAUTION: Downtrend detected"
    elif coin["price_trend"] == "volatile":
        profit_advice = "🎢 High volatility - Dollar-cost averaging recommended"
    else:
        profit_advice = "🔄 Hold (stable price action)"

    # Sustainability Rules
    energy_icons = {"high": "⚡", "medium": "🔋", "low": "🌱"}
    sustain_advice = f"{energy_icons[coin['energy_use']]} Energy: {coin['energy_use'].upper()}"

    # Risk Assessment
    risk_emoji = "☠️" if coin["risk_score"] >=7 else "⚠️" if coin["risk_score"] >=5 else "🛡️"
    
    return f"""
📊 {coin_name.upper()} ANALYSIS (2025-06-13):
- Profitability: {profit_advice}
- Sustainability: {sustain_advice}
- Risk: {risk_emoji} Score {coin['risk_score']}/10
"""

# Chat Interface
print("🌟 CRYPTO ADVISOR: Ask about Bitcoin/Ethereum/Solana/Cardano (type 'quit' to exit)")
while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() == "quit":
        print("Bot: Goodbye! 👋")
        break
    print("Bot:", get_advice(user_input))
