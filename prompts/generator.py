def generate_prompt_yaml(user_input: str, lang: str = "en") -> str:
    if lang == "ru":
        return f"""
промт:
  роль: "АРХИТЕКТОР ПРОМТОВ"
  задача: "{user_input}"
  предположения: ["уточнений нет"]
  шаги: ["Прямой проход", "Loss", "Backprop", "Optimizer"]
  формат: "YAML"
  источник: ["Prompt v1.2"]
""".strip()
    else:
        return f"""
prompt:
  role: "Prompt Architect"
  task: "{user_input}"
  assumptions: ["not specified"]
  steps: ["Forward pass", "Loss", "Backpropagation", "Optimizer step"]
  format: "YAML"
  provenance: ["Prompt v1.2"]
""".strip()

