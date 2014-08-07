Как принять участие в проекте?
=======================================

Вначале нам необходимо настоить виртуальное окружение для нашего проекта:

	virtualenv ~/.env
	source ~/.env/bin/activate


Затем создадим клон репозитория:

	git clone git@github.com:aliev/runestone.git
	cd runestone
	git submodule init
	git submodule update

Установим зависимости

	sudo apt-get install gcc-snapshot build-essential libxml2-dev python-dev
	pip install -r requirements.txt

Книга находится в директории source в формате ReStructuredText. Изначально редактируются rst файлы, затем уже выполняется сборка книги следующей командой:

	paver allbooks

Можно открыть сборку и посмотреть результат работы:

    open static/pythonds/index.html
