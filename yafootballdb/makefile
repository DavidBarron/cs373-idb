# http://www.gnu.org/software/make/

FILES :=                \
    .gitignore          \
    .travis.yml         \
    apiary.apib         \
    IDB.log             \
    models.html         \
    models.py           \
    tests.py            \
    UML.pdf             \
    tests.out			\

all:

check:
	@for i in $(FILES);                                     \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

models.html: models.py
	pydoc3 -w models

IDB.log:
	git log > IDB.log

test: test.out

test.out: tests.py
	coverage3 run    --branch manage.py shell < tests.py > tests.out 2>&1
	coverage3 report -m                      >> tests.out
	cat tests.out

