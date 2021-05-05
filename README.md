# Rūrusetto (ルールセット)

 [![Netlify Status](https://api.netlify.com/api/v1/badges/dda6b2bf-05d7-4d90-ad9d-b2a4c1bca8fa/deploy-status)](https://app.netlify.com/sites/osu-ruleset/deploys)
 [![Discord Shield](https://discordapp.com/api/guilds/700619421466624050/widget.png?style=shield)](https://discord.gg/CQPNADu)

 A wiki that contain all osu! rulesets

## Domain

- Dev build (Some function in dark mode like color invert will not work.) : https://dev.rulesets.info/
- Official build : https://rulesets.info/
- Directly to a ruleset page : https://[rulesetname].rulesets.info/

## Development Status

A website structure is almost finish. Current adding more ruleset to website.

## Developing Rūrusetto codebase

*If you don't want to developing a codebase but you want to contribute a wiki you can skip to [contributing](#contributing) part.*

Please make sure you have the following prerequisites:

- [Hugo Framework](https://gohugo.io/)
- Text IDE. We recommend IDE with intelligent code completion and syntax highlighting if you work with a codebase. Our recommendation is [Visual Studio Code](https://code.visualstudio.com/)

### Downloading the source code

Clone the repository:

```shell
git clone https://github.com/ppy/osu
cd osu
```

To update the source code to the latest commit, run the following command inside the Rūrusetto directory:

```shell
git pull
```

### Start a development server

Run this command inside the Rūrusetto directory, this will enable a development in http://localhost:1313/ and this support fast render and reload:

```shell
hugo server
```

### Build this website

Run this command inside the Rūrusetto directory, complete build will available in `public` directory inside source code directory.

```shell
hugo
```

## Contributing

Please see [the "contributing" file](CONTRIBUTING.md) if you are interested in helping out with the project!

## Disclaimer

Pippi icon : [@annytf](https://twitter.com/annytf/status/991050258183434240)

Default ruleset icon : [osu-resources](https://github.com/ppy/osu-resources)

## License

The majority of content in this repository is licensed under MIT license. Please see [the license file](LICENSE) for more information. tl;dr you can do whatever you want as long as you include the original copyright and license notice in any copy of the software/source.

Each rulesets has its own license.

The licensing here does not directly apply to `osu!` and `ppy`, as it is bound to its own licensing.
