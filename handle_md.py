import datetime
import re
import sys


# BEFORE
#     <img src="D:\Desktop\images\2020\go_to_school.jpg" alt="go_to_school" style="zoom:40%;" />
# AFTER run >> python3 handle_md.py 2020 05 test
#     {{< img src="/images/2020/05/test/go_to_school.jpg" alt="go to school" width="80%" >}}


def file_handler(file_name, year=None, month=None, folder_name='default'):
    path = '/images/' + year + '/' + month + '/' + folder_name + '/'
    rule = re.compile(r'<img src=".*\\(.*\.jpg)" alt="(.*)" style=".*;" />')
    with open(file_name, 'r', encoding="utf-8") as raw:
        with open('output.md', 'w', encoding="utf-8") as new:
            for line in raw.readlines():
                txt = re.search(rule, line)
                if txt is not None:
                    pass
                    image_name, alt_name = txt.groups()
                    alt_name = alt_name.replace('_', ' ')
                    src = path + image_name

                    img_src = '{{< img src=\"' + src + '\" ' + 'alt=\"' + alt_name + '\" ' + 'width=\"80%\" >}}' + '\n'
                    print(img_src)

                    new.write(img_src)
                else:
                    new.write(line)
    print('Done')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        today = datetime.datetime.now()
        file_handler(
            'file.md',
            year=str(today.year) if today.year > 10 else '0' + str(today.year),
            month=str(today.month) if today.month > 10 else '0' + str(today.month)
        )
    elif len(sys.argv) == 2:
        today = datetime.datetime.now()
        file_handler(
            'file.md',
            year=str(today.year) if today.year > 10 else '0' + str(today.year),
            month=str(today.month) if today.month > 10 else '0' + str(today.month),
            folder_name=sys.argv[1]
        )
    elif len(sys.argv) == 4:
        file_handler(
            'file.md',
            year=sys.argv[1],
            month=sys.argv[2],
            folder_name=sys.argv[3]
        )
    else:
        print('try:\n\tpython3 handle_md.py\n\tpython3 handle_md.py FOLDER_NAME\n\tpython3 handle_md.py YEAR MONTH FOLDER_NAME')
