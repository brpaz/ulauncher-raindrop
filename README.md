# ulauncher-raindrop

> Search in your [Raindrop](https://raindrop.io/) bookmarks directly from [Ulauncher](https://ulauncher.io/).

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-yellowgreen.svg?style=for-the-badge)](https://ext.ulauncher.io/)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-raindrop/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-raindrop)
[![License](https://img.shields.io/github/license/brpaz/ulauncher-raindrop.svg?style=for-the-badge)](LICENSE)

## Features

* Search on your entire collection of Bookmarks.
* Open a selected bookmark in the default browser
* Open `https://app.raindrop.io` using the `rdopen` keyword

![demo](demo.gif)

## Requirements

* [Ulauncher](https://github.com/Ulauncher/Ulauncher) > 5.0
* Python >= 3.7
* python-raindropio - `pip install --user python-raindropio==0.0.4`

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-raindrop
```

## Usage

### Configurations

To be able to do calls to the Raindrop API you must create an access token and set it´s value on the extension settings.

To generate a new token, go to [Integrations page](https://app.raindrop.io/settings/integrations) on Raindrop, and select `Create a new App` in the `Developers`section. Give in a name like `Ulauncher Extension`.

After the app is created, click on it to open the details and create a "Test Token".

### Keywords

The following keywords are specified by this extension:

* ```rd <query>``` to to search on all your bookmarks.
* ```rdopen``` to open Raindrop Web App.
* ```rdunsorted``` to search on your `Unsorted` bookmarks

## Development

```
git clone https://github.com/brpaz/ulauncher-raindrop
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `make dev`.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💛 Support the project

If this project was useful to you in some form, I would be glad to have your support.  It will help to keep the project alive and to have more time to work on Open Source.

The sinplest form of support is to give a ⭐️ to this repo.

You can also contribute with [GitHub Sponsors](https://github.com/sponsors/brpaz).

[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sponsor%20Me-red?style=for-the-badge)](https://github.com/sponsors/brpaz)

Or if you prefer a one time donation to the project, you can simple:

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee"
style="height: auto !important;width: auto !important;" ></a>

---
## License

MIT &copy; Bruno Paz
