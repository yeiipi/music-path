

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


def get_tokenb() :
    print('Buscando Token...')
    driver = webdriver.Firefox()

    driver.get('https://developer.spotify.com/console/get-artist-related-artists/?id=asdfsdfasdf')
    get_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/article/div[3]/div/div/form/div[3]/div/span/button')


    get_button.click()
    sleep(1)
    request_token_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/article/div[3]/div/div/div[1]/div/div/div[2]/form/input')
    sleep(0.5)
    request_token_button.click()


    # login   |jue sep 24 11:25:45 -05 2020|
    cuenta = 'nosoymalloc@gmail.com'
    contraseña = 'E18iO1JSoZZc2jiw75fZqeH6lp582?t'
    logid = 'login-username'
    passwid = 'login-password'


    account_button = driver.find_element_by_id(logid)
    login_button = driver.find_element_by_id('login-button')
    passwd_button = driver.find_element_by_id('login-password')


    account_button.send_keys(cuenta)
    passwd_button.send_keys(contraseña)
    login_button.click()


    # ahora acepto   |jue sep 24 11:38:01 -05 2020|
    sleep(2)
    agree_button = driver.find_element_by_id('auth-accept')
    agree_button.click()


    # ahora agarro el token   |jue sep 24 11:39:30 -05 2020|
    sleep(2)
    token_box = driver.find_element_by_id('oauth-input')
    token = token_box.get_attribute('value')


    #ciero el browser   |jue sep 24 12:02:45 -05 2020|
    driver.close()
    return(token)


# def get_artist_id(artista):
#
#     print('Buscando Id del artista...')
#     driver = webdriver.Firefox()
#
#     # Entrar a google y encontrar la barra de busqueda | 25.09.2020 | jpi
#     driver.get('https://google.com')
#     barra_de_busqueda = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
#
#     sleep(1)
#
#     # Realizar la busqueda del artista | 25.09.2020 | jpi
#     barra_de_busqueda.send_keys(f"{artista} On Spotify")
#     barra_de_busqueda.send_keys(Keys.RETURN)
#
#     sleep(2)
#
#     # Entrar a spotify | 25.09.2020 | jpi
#     spotify_boton = driver.find_element_by_partial_link_text('spotify')
#     spotify_boton.click()
#
#     sleep(2)
#
#
#     # obtener id a partir del url de la pag de Spotify | 25.09.2020 | jpi
#     pagina_artista = driver.current_url
#     artista_id = pagina_artista[32:]
#
#
#     # cierro browser | 25.09.2020 | jpi
#     driver.close()
#
#     return artista_id
