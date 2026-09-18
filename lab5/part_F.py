def create_report(title: str, *sections: dict[str, str | list[str]], **metadata: str | bool) -> dict:
    report = {"title": title}
    report["sections"] = list(sections)
    report["metadata"] = metadata
    return report

"""
I choose to represent each section as a dictionary, with the following keys:
    - heading: str
    - paragraphs: list[str]
"""

def summarize_report(report: dict):
    for item in report.items():
        print("Dictionary item", item)
    summary = [report.get("title")]
    metadata = report.get("metadata")
    sections = report.get("sections", ())

    if metadata:
        for key, value in metadata.items():
            summary.append(f"{key.title()}: {value}")
        summary.append("\n")

    for value in sections:
        summary.append(value.get("heading"))
        paragraphs = (value.get("paragraphs", []))
        for paragraph in paragraphs:
            summary.append(paragraph)
        summary.append("\n")
        
    return "\n".join(summary)

first_section = {"heading": "Computing machines", "paragraphs": ["This is the first section paragraph.", "Second paragraph."]}
second_section = {"heading": "Definitions", "paragraphs": ["This is the second section paragraph."]}
third_section = {"heading": "Examples", "paragraphs": ["This is the third section paragraph.", "Final paragraph."]}

report = create_report("On Computable Numbers", first_section, second_section, third_section, 
                       author="Alan Turing", department="Computer Science", version="1.0", 
                       confidential=False, date="November 12 1936")
print(summarize_report(report))