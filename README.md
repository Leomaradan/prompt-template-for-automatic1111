# Prompt Template

This is an extension for [AUTOMATIC1111 Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui).

It add a new panel in Extra Data containing prompt template. Prompt template are simply a text file with extension `*.tpl` or `*.template`. When clicking of the card, the content of the file is added to the prompt.

This extension solve the problem of LORA Weight and trigger, as each Lora can have a different recommended weight, some optional trigger word, etc. 

For example, the Lora [Tifa Lockhart (Final Fantasy VII) LoRA](https://civitai.com/models/87167/tifa-lockhart-final-fantasy-vii-lora-or-7-outfits) has 7 outfits with specifics triggers. With this extension, you can create seven `.tpl` files in the `templates` folder, one for each variation. Each template can include it's preview image and description file

![image](https://i.imgur.com/BC9o487.png)

## Creating a template file

For creating a template file, simple open the stable-diffusion-webui. You should see a `templates` folder. If it's not there, you can create it. In this `templates` folder, you can also create subfolder to organize your prompt templates.

You can now create a new txt file with the wanted name (from above example: `tifa-original.txt`). Open the created file, and type (or paste) your prompt. Save the file, and change the extension to `.tpl`. If you want a preview image, you can simple put an image with the same name in the folder. You can also create a new file but with `.txt`, and the content of this file will be used to display a description in the extra network card

![image](https://i.imgur.com/uW9caVO.png)

## Hiding network tabs

This extension also add the option in Settings > Extra Networks > Hide Extra networks tab.
With this option, you can hide unused Extra Networks tabs