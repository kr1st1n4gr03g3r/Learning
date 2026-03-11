1) If you want to select a chunk of text from one portion to another, eg:

`<a href="/apple/ios-11.1/smiling-face-with-open-mouth-and-cold-sweat/">
<img src="https://emojipedia-us.s3.amazonaws.com/thumbs/72/apple/114/smiling-face-with-open-mouth-and-cold-sweat_1f605.png" srcset="https://emojipedia-us.s3.amazonaws.com/thumbs/144/apple/114/smiling-face-with-open-mouth-and-cold-sweat_1f605.png 2x" alt="Smiling Face With Open Mouth &amp; Cold Sweat" title="Smiling Face With Open Mouth &amp; Cold Sweat" width="72" height="72">`

`<a href="[^"]*">` will select `<a href="` and everything in-between it up until `">"`

2) Replace text before specific text:

Eg: Select everything before "R_"

`^.*?(?=/R_)` 
or: 
`(?<=/)[^/]+$`

3) Select all text after specific text:
Eg: Select everything after the last "/"

`(?<=/)[^/]+$`

<img width="386" height="286" alt="image" src="https://github.com/user-attachments/assets/81896f15-c243-4eff-98a3-52c86cc944da" />
