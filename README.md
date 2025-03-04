# Google-Translator
This Python script utilizes the googletrans library to allow users to translate text into various languages interactively. The script provides a user-friendly interface for language selection and translation with the following features:

#### Key Features:

1. **Language Selection:**
   - The script defines a dictionary `language` containing language codes and their corresponding language names (e.g., "en" for English, "fr" for French).
   - Users can type "options" to view the list of available language codes.
   - Users input their desired language code, which is validated against the dictionary to ensure it's a valid option.

2. **Interactive Translation Loop:**
   - Once a valid language code is selected by the user, the script enters an interactive loop.
   - Users can input text they want to translate, and the text is translated into the previously selected language.
   - If users input "close", the program exits the loop and terminates.

3. **Asynchronous Translation:**
   - The translation feature is implemented using asynchronous functions to improve efficiency and handle potential delays in translation services.
   - The function `translate_text` performs the translation asynchronously using the `googletrans` Translator object.
   - The `asyncio` library is used to manage asynchronous operations and ensure the event loop is properly created and executed.

#### Code Structure:

- **Language Dictionary:**
  - A dictionary named `language` contains language codes as keys and corresponding language names as values.

- **Language Code Selection:**
  - The script asks users for their desired language code.
  - If the input is "options", the script prints out all available language codes and their corresponding languages.
  - If a valid language code is entered, it is selected for translation.

- **Translation Loop:**
  - The script repeatedly prompts users to enter the text they want to translate.
  - If "close" is entered, the script prints a goodbye message and exits the loop.
  - The translation is performed asynchronously using the `translate_text` function, which translates the text using `googletrans` and prints the translated text, pronunciation, and source language.

- **Asynchronous Handling:**
  - The code uses `asyncio.run(main())` to run the main coroutine, which handles the translation loop and ensures proper creation and management of the event loop.

#### Error Handling:

- The script includes a try-except block within the `translate_text` function to handle potential errors during translation, ensuring that users are informed if any issues occur.

Overall, this script provides an easy-to-use command-line interface for text translation, leveraging the capabilities of the `googletrans` library and the `asyncio` module for efficient and responsive translations.

---

This description provides a detailed overview of the script's functionality, structure, and key features.
