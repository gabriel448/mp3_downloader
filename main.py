from pytube import Playlist
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, VideoPrivate, AgeRestrictedError
import os
from pathlib import Path
import sys
from colorama import Fore, Style

def audio_dowloader_unic(url, local):
    try:
        audio_url = YouTube(url)
        print(f'********** baixando {audio_url.title} **********')
        print()
        print(Style.DIM + '⌛ Downloading ⌛')
        audio = audio_url.streams.get_by_itag(251)
        diretorio = (fr'{local}')
        download_file = audio.download(diretorio)
        base, ext = os.path.splitext(download_file)
        new_file = base + '.mp3'
        os.rename(download_file, new_file)
        sys.stdout.write('\033[F')
        print(Style.NORMAL + '✅ Download completo ✅')
    except FileExistsError:
        os.sytem('cls')
        print('!! Ja esxite um arquivo como este neste diretorio !!')
    except VideoPrivate:
        print(Style.NORMAL + '')
        print(Fore.RED + f'!!{Fore.CYAN} "{audio_url.title}" Eh um video privado{Fore.RED} !!')
        print(Fore.RESET + '')
    except AgeRestrictedError:
        print(Style.NORMAL + '')
        print(Fore.RED + f'!!{Fore.CYAN} "{audio_url.title}" Eh um video com resticao de idade{Fore.RED} !!')
        print(Fore.RESET + '')
    except AttributeError:
        print(Style.NORMAL + '')
        print(Fore.RED + f'!!{Fore.CYAN} "{audio_url.title}" Eh um video invalido (nao esta disponivel para download){Fore.RED} !!')
        print(Fore.RESET + '')
    

def playlist_donwloader(url, local):
    try:
        audios_url = Playlist(url)
        diretorio = (fr'{local}\{audios_url.title}')
        folder_name = f'{audios_url.title}'
        path = os.path.join(local, folder_name)
        os.mkdir(path)
        print(f'********** Baixando {audios_url.title} **********')
        print()
        for audio in audios_url:
            try:
                audio_url = YouTube(audio)
                print(Style.DIM + f'{audio_url.title} - ⌛')
                audio = audio_url.streams.get_by_itag(251)
                download_file = audio.download(diretorio)
                base, ext = os.path.splitext(download_file)
                new_file = base + '.mp3'
                os.rename(download_file, new_file)
                sys.stdout.write("\033[F")
                print(Style.NORMAL + f'{audio.title} - ✅')
            except VideoPrivate:
                print()
                print(Fore.RED + f'!!{Fore.CYAN} "{audio_url.title}" Eh um video privado{Fore.RED} !!')
                print(Fore.RESET + '')
            except AgeRestrictedError:
                print()
                print(Fore.RED + f'!!{Fore.CYAN} "{audio_url.title}" Eh um video com resticao de idade{Fore.RED} !!')
                print(Fore.RESET + '')
            except AttributeError:
                print()
                print(Fore.RED + f'!!{Fore.CYAN} "{audio_url.title}" Eh um video invalido (nao esta disponivel para download){Fore.RED} !!')
                print(Fore.RESET + '')
        print('✅ Download completo ✅')
    except FileExistsError:
        os.system('cls')
        print('Ja esxite uma playlist como esta neste diretorio')



url = None
local = None

while True:
    i = True
    i_2 = None
    print(Fore.CYAN + '*************** Downloader .MP3 ***************')
    print(Fore.RESET + '')
    p_or_v = input('Deseja baixar uma [P]laylist ou um [A]udio?: ').lower()
    if p_or_v.startswith('p'):
        url = input('Digite a link da playlist: ')
        if 'https://www.youtube.com' not in url:
            os.system('cls')
            print('LINK INVALIDO')
            print()
            continue
    elif p_or_v.startswith('a'):
        url = input('Digite a link do audio: ')
        if 'https' not in url:
            os.system('cls')
            print('LINK INVALIDO')
            print()
            continue
    else:
        os.system('cls')
        print('COMANDO INVALIDO')
        print()
        continue

    if local == None:
        local = input('Digite o diretorio para o download: ')
    
    if p_or_v.startswith('p'):
        playlist_donwloader(url, local)
    elif p_or_v.startswith('a'):
        audio_dowloader_unic(url, local)
    
    print()
    while i:
        choise = input('Deseja fazer outro download?: ').lower()
        
        if choise.startswith('s'):
            os.system('cls')
            i = False

        elif choise.startswith('n'):
            os.system('cls')
            print('Sessao fechada...')
            i = False
            i_2 = True
        else:
            os.system('cls')
            print('!!!Comando invalido!!!')
            continue
    if i_2:
        break
        