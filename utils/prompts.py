def get_prompt(age_group: str, tone: str, length: str) -> str:
    length_instruction = {
        "Short": "Keep the message brief (30–50 words).",
        "Medium": "Make the message moderately detailed (60–100 words).",
        "Long": "Feel free to elaborate in detail (more than 100 words)."
    }.get(length, "")

    base_prompts = {
        "kids": "Write ONE {tone} and exciting marketing message for kids about the product: {product}. Use simple, playful language. {length_instruction} Only return a single full message.",
        "adults": "Write ONE {tone} and persuasive marketing message for adults about the product: {product}. Focus on value and practicality. {length_instruction} One message only.",
        "seniors": "Write ONE {tone} and clear marketing message for seniors about the product: {product}. Emphasize comfort and ease of use. {length_instruction} Return one full message."
    }

    return base_prompts.get(age_group.lower(), base_prompts["adults"]).replace("{length_instruction}", length_instruction)
