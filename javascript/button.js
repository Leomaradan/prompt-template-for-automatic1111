function cardClickedAddOnly(textToAdd, allowNegativePrompt) {
  var tabname = gradioApp().querySelector('#tabs > div[style="display: block;"]').id.replace("tab_", "");
  var textarea = allowNegativePrompt ? activePromptTextarea[tabname] : gradioApp().querySelector("#" + tabname + "_prompt > label > textarea");

  if (textarea) {
    textarea.value = textarea.value + opts.extra_networks_add_text_separator + textToAdd;
  }

  updateInput(textarea);
}
