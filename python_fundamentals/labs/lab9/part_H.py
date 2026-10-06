class Exporter:
    def export(self, data):
        return data

class ConsoleExporter(Exporter):
    def export(self, data):
        return f"Console {str(data)}"

    def __str__(self):
        return "Console exporter"

class TextExporter(Exporter):
    def export(self, data):
        return f"Text {str(data)}"

    def __str__(self):
        return "Text exporter"

class Title:
    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        return self.title.strip().title()

class SummaryExporter(Exporter):
    def __init__(self, title: Title):
        self.title = title

    def export(self, data):
        return (
            f"{self.title}\n"
            f"Summary {str(data)}"
        )

    def __str__(self):
        return "Summary exporter"

class UnrelatedExporter:
    def export(self, data):
        return data

    def __str__(self):
        return "Unrelated exporter"

data = "Testing data"
title = Title("Summary title")
console = ConsoleExporter()
text = TextExporter()
summary = SummaryExporter(title)
unrelated = UnrelatedExporter()
exporters = [console, text, summary, unrelated]

for exporter in exporters:
    print(f"{exporter.export(data)} exported by {str(exporter)}")

print(isinstance(console, Exporter))
print(isinstance(text, Exporter))
print(isinstance(summary, Exporter))
print(isinstance(unrelated, Exporter))
print(isinstance(console, TextExporter))

# The example of compsition in this program is the Title class that is used in the SummaryExporter.
# SummaryExporter has-a Title