import regex as re

texto = "asadasd mente asdhsad"
for m in re.finditer(r"\w+mente\b",texto):
	print(m.start(),m.end(),m.group(0))
    