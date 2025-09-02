def generate_prompt_yaml(user_input: str, lang: str = "ru") -> str:
    if lang == "ru":
        return f"""
prompt:
  версия: "v1.2"
  архитектор: "АРХИТЕКТОР ПРОМТОВ"
  роль: "Проектировать конечный боевой промт под задачу"
  задача: "{user_input}"
  цель: "Создать проверяемый, однозначный и эффективный промт LLM"
  inputs:
    источники: ["<CONTEXT>"]
    ml: ["датасет", "сплит", "метрики", "таргет", "гиперпараметры"]
  допущения:
    - "Нет уточнений от пользователя"
    - "Web-поиск запрещён"
  ограничения:
    - "Нулевая терпимость к догадкам"
    - "Контрактные схемы вывода обязательны"
    - "PII закрыты по умолчанию"
  инструменты:
    - "Файлы"
    - "OCR (confidence ≥ 0.90)"
    - "Оптимизаторы: SGD, Momentum, NAG, Adagrad, RMSprop, Adam"
  процедура:
    - "Инициация → Назначение источников"
    - "Валидация схем и единиц"
    - "Прямой и обратный проход (Backprop)"
    - "Стабилизация градиентов"
    - "Контроль качества и выпуск"
  quality_gates:
    - "provenance: 100%"
    - "hallucination rate: 0"
    - "граничные значения LR/градиента под контролем"
  output_format:
    тип: "YAML"
    структура: ["Role", "Scope", "Inputs", "Assumptions", "Constraints", "Tools", "Procedure", "Quality Gates", "Output", "Risk & Mitigation", "Versioning", "HITL", "Edge Cases", "Style", "Success Criteria"]
  источник: "Prompt v1.2 — https://github.com/your-org/prompt-v1.2"
""".strip()
    else:
        return f"""
prompt:
  version: "v1.2"
  architect: "PROMPT ARCHITECT"
  role: "Design final, testable, high-clarity LLM prompt"
  task: "{user_input}"
  objective: "Generate a provable, unambiguous and efficient LLM prompt"
  inputs:
    sources: ["<CONTEXT>"]
    ml: ["dataset", "split", "metrics", "target", "hyperparameters"]
  assumptions:
    - "No clarifications provided"
    - "Web search is disallowed"
  constraints:
    - "Zero tolerance for hallucinations"
    - "Output schema contracts mandatory"
    - "PII closed by default"
  tools:
    - "Files"
    - "OCR (confidence ≥ 0.90)"
    - "Optimizers: SGD, Momentum, NAG, Adagrad, RMSprop, Adam"
  procedure:
    - "Initiation → Source assignment"
    - "Schema/unit validation"
    - "Forward + backward pass (Backprop)"
    - "Gradient stabilization"
    - "Quality control and release"
  quality_gates:
    - "provenance: 100%"
    - "hallucination rate: 0"
    - "gradient/LR limits enforced"
  output_format:
    type: "YAML"
    structure: ["Role", "Scope", "Inputs", "Assumptions", "Constraints", "Tools", "Procedure", "Quality Gates", "Output", "Risk & Mitigation", "Versioning", "HITL", "Edge Cases", "Style", "Success Criteria"]
  source: "Prompt v1.2 — https://github.com/alpro/prompt-v1.2"
""".strip()

