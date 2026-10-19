import json
from datetime import datetime

def update_json_file():
    comprehensive_meta_data = [
        {
            "rank": 1,
            "character_item": "Apocalypse (Big Boy)",
            "category": "Legendary / Arena Meta",
            "tier": "S+",
            "meta_score": 99.4,
            "resource_efficiency": "High (Strict ROI)",
            "daily_trend": "+4.2%",
            "primary_role": "Controller / Brawler",
            "verification_source": "MSF.gg Roster & Reddit Consensus"
        },
        {
            "rank": 2,
            "character_item": "Super Skrull",
            "category": "Global / Raid",
            "tier": "S+",
            "meta_score": 98.1,
            "resource_efficiency": "Medium",
            "daily_trend": "+1.5%",
            "primary_role": "Blaster / Support",
            "verification_source": "Community Cross-Ref #7 & ValleyFlyin Metrics"
        },
        {
            "rank": 3,
            "character_item": "Mephisto",
            "category": "Dimension Battle / Arena",
            "tier": "S+",
            "meta_score": 98.9,
            "resource_efficiency": "Low (Extreme Cost)",
            "daily_trend": "+5.8%",
            "primary_role": "Controller",
            "verification_source": "Top 10 Arena Analytics"
        },
        {
            "rank": 4,
            "character_item": "Odin",
            "category": "Crucible / War",
            "tier": "S+",
            "meta_score": 97.5,
            "resource_efficiency": "High",
            "daily_trend": "+3.1%",
            "primary_role": "Controller / Brawler",
            "verification_source": "Illuminati Meta Cross-Ref"
        },
        {
            "rank": 5,
            "character_item": "Black Knight",
            "category": "Arena Defense",
            "tier": "S",
            "meta_score": 95.8,
            "resource_efficiency": "Very High",
            "daily_trend": "-0.8%",
            "primary_role": "Protector",
            "verification_source": "MSF Discord Metrics & Community Tier List"
        },
        {
            "rank": 6,
            "character_item": "Gladiator",
            "category": "Cosmic / Arena",
            "tier": "S",
            "meta_score": 94.7,
            "resource_efficiency": "High",
            "daily_trend": "+2.0%",
            "primary_role": "Protector",
            "verification_source": "MSF.gg Live Data v24"
        },
        {
            "rank": 7,
            "character_item": "Thanos (Endgame)",
            "category": "Raid / War",
            "tier": "S",
            "meta_score": 93.9,
            "resource_efficiency": "Medium",
            "daily_trend": "+0.4%",
            "primary_role": "Brawler",
            "verification_source": "KrakFest Analytics"
        },
        {
            "rank": 8,
            "character_item": "Nightstalker - Blade",
            "category": "Mystic / Raid",
            "tier": "S",
            "meta_score": 93.2,
            "resource_efficiency": "Very High",
            "daily_trend": "+1.1%",
            "primary_role": "Brawler",
            "verification_source": "Raid Team Synergy Report"
        },
        {
            "rank": 9,
            "character_item": "Professor X",
            "category": "Global / Legendary",
            "tier": "S+",
            "meta_score": 99.1,
            "resource_efficiency": "Low (High Gate)",
            "daily_trend": "+2.9%",
            "primary_role": "Support",
            "verification_source": "Global Top Alliance Consensus"
        },
        {
            "rank": 10,
            "character_item": "Hank Pym",
            "category": "Tech / Raid",
            "tier": "A+",
            "meta_score": 91.5,
            "resource_efficiency": "High",
            "daily_trend": "-1.2%",
            "primary_role": "Support",
            "verification_source": "Community Meta Watch"
        },
        {
            "rank": 11,
            "character_item": "Shuri (Extremis)",
            "category": "Tech / Raid",
            "tier": "A+",
            "meta_score": 90.8,
            "resource_efficiency": "High",
            "daily_trend": "+0.5%",
            "primary_role": "Controller",
            "verification_source": "MSF.gg Roster Stats"
        },
        {
            "rank": 12,
            "character_item": "Sentinel",
            "category": "Tech / War",
            "tier": "A+",
            "meta_score": 89.9,
            "resource_efficiency": "Medium",
            "daily_trend": "+1.8%",
            "primary_role": "Protector",
            "verification_source": "War Defense Meta Review"
        }
    ]

    # כתיבה ישירה של הנתונים אל קובץ ה-JSON
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(comprehensive_meta_data, f, indent=2, ensure_ascii=False)
    
    print(f"data.json successfully updated at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")

if __name__ == "__main__":
    update_json_file()
