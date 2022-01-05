# if37_projet_2021-2022
Site web permettant de transformer des textes en textes ayant une écriture inclusive

### Nécessaire

- Python3
  - pip3

- Tesseract-OCR : permet la reconnaissance de text
  - module de texte français

  

### Mise en place

#### Environnement python

```sh
pip install -r requirement.txt
```

#### Environnement Tesseract

Insérer le chemin de l’exécutable de Tesseract dans main.py (ligne 9) :

```python
# Example pour windows: r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'<chemin_vers_tesseract_exe>'
```

### Exécution

```shell
python3 app.py
```

