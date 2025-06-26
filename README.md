# Fancaps Direct URL Downloader

A simple **Google Colab** compatible Python script to download manually selected image URLs from [Fancaps.net](https://fancaps.net).  
This tool does **not** perform bulk scraping — instead, it precisely downloads only the URLs you provide.

---

## Features

- Download any list of direct image URLs from Fancaps CDN (`cdni.fancaps.net`)  
- Easy to customize: just paste your URLs into the script  
- Parallel downloads for faster performance  
- Compatible with Google Colab or any Python 3 environment  
- Optional support for Cloudflare `cf_clearance` cookie (for protected content)

---

## Open in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/citronlegacy/fancaps-direct-url-downloader/blob/main/fancaps_direct_url_downloader_COLAB.ipynb)


## Usage

1. Open the script in Google Colab or your favorite Python environment.  
2. Paste your list of Fancaps image URLs (one per line) inside the `urls_text` variable.  
3. (Optional) Add your `cf_clearance` cookie if needed to bypass Cloudflare protection.  
4. Run the script — images will be saved to the specified output folder (`./downloads/test3` by default).

---

## Example URLs format
https://cdni.fancaps.net/file/fancaps-movieimages/4839637.jpg
https://cdni.fancaps.net/file/fancaps-movieimages/4839642.jpg
https://cdni.fancaps.net/file/fancaps-movieimages/4839650.jpg


---

## Credits

Inspired by [KitsunekoFi's fancaps-dl](https://github.com/KitsunekoFi/fancaps-dl), a more advanced downloader for Fancaps.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
