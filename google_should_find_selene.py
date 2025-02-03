from selene import browser, be, have

def test_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))
    #should(be.blank) - проверка(should), что поле должно быть пустым?

def test_yandex():
    browser.open('https://ya.ru/')
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
