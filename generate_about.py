from horoscope import get_times, get_advices, get_promises
from datetime import datetime as dt

def generate_page(head, body):
	page = f"<html>{head}{body}</html>"
	return page

def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>
	"""
	return head

def generate_body(header, times, advices, promises):
	body = f"<h1>{header}</h1><br/><br/><img src='horoscope.jpg' width='100' height='100'><br/>"
	body +="<ol><li>Время дня:</li><ul>"
	for t in times:
		body += f"<li>{t}</li>"
	body += "</ul><li>Глаголы</li><ul>"
	for a in advices:
		body += f"<li>{a}</li>"
	body += "</ul><li>Пожелания</li><ul>"
	for p in promises:
		body += f"<li>{p}</li>"
	body += "</ul></ol>"	

	return f"<body>{body}</body>"

def save_page(title, header,  times, advices, promises, output="about.html"):
	fp = open(output, "w", encoding='utf-8')
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header,  times=times, advices=advices, promises=promises)
	)
	print(page, file=fp)
	fp.close()

#####################

today = dt.now().date()
save_page(
	title="О реализации",
	header="О чем всё это",
	times=get_times(),
	advices=get_advices(),
	promises= get_promises()
)