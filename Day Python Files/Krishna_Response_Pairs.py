import json

# Load your dialogue JSON
with open("../Text Files/gita_dialogue.json", "r", encoding="utf-8") as f:
    dialogue_data = json.load(f)

# Create instruction-response pairs
instruction_response_pairs = []

for i in range(len(dialogue_data) - 1):
    current = dialogue_data[i]
    next_ = dialogue_data[i + 1]
    
    if current["speaker"] != "Lord Krishna" and next_["speaker"] == "Lord Krishna":
        instruction = f"{current['speaker']} said: {current['text']}"
        response = f"Lord Krishna replied: {next_['text']}"
        instruction_response_pairs.append({
            "instruction": instruction,
            "response": response
        })

# Save to JSON
with open("krishna_instruction_response.json", "w", encoding="utf-8") as f:
    json.dump(instruction_response_pairs, f, ensure_ascii=False, indent=2)

print("✅ Saved Krishna-style instruction-response dataset.")
