from googletrans import Translator

def translator(text, dest):
    trans = Translator()
    
    response = trans.translate(text, dest)
    return response

def main():
    lang_dict = {'zh-cn' : 'Chinese', 'nl' : 'Dutch', 'en' : 'English', 'fr' : 'French', 'de' : 'German', 'el' : 'Greek', 'it' : 'Italian', 
                'ja' : 'Japanese', 'ko' : 'Korean', 'la' : 'Latin', 'pl' : 'Polish', 'pt' : 'Portuguese', 'es' : 'Spanish',
                'sv' : 'Swedish', 'th' : 'Thai', 'vi' : 'Vietnamese', 'cy' : 'Welsh'}
    
    text = input("\nEnter the text: ")
    print("\nAvailable Language Codes: ", lang_dict)
    
    dest = input("\nEnter the target language code: ")
    
    translated_text = translator(text, dest)
    
    print(f"\nTranslated text: {translated_text.text}\n")
    
if __name__ == "__main__":
    main()