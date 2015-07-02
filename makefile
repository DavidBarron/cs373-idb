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

all:

check:
	@for i in $(FILES);                                     \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

