# python gantt lib

This project is an extension of the `python-gantt` module, providing some extra functionality.
This includes some translation to spanish of the days and months, new classes for add hyperlinks to the tasks and projects, and svg in format string for using it as context in Django lib.

## Instalation

Run the following to install:

```
pip install gantt-lib-lautarodapin
```

## Aditional requirements

* Library: `python-gantt` see [link](https://pypi.org/project/python-gantt/)
* Author: Alexandre Norman (norman at xael.org)
 

## Usage
```python

import gantt_lib
import datetime
resource = gantt_lib.Resource("Resource 1")

project = gantt_lib.HiperLinkedProject(
                                      name='Project', 
                                      link='mypage/link/to/project',
                                      target='_self' #HTML target (it opens the link on the same page)
                                      )

project.add_task(gantt_lib.HyperLinkedTask(
    name= 'task 1',
        start=datetime.datetime.date(2020,7,1),
        duration=5,
        resources=[resource],
        percent_done=0,
        color="#03d529",
        link_name='mypage/link/to/title',
        link_resource='mypage/link/to/resource',
        link_lateral='mypage/link/to/extra',
        target='_self' #HTML target (it opens the link on the same page)
    )
)

# make_svg_for_task returns the xml code in string format, this way you can use it as context in django or flask
# also saves it into a file
svg = project.make_svg_for_tasks(
        'file.svg', 
        today=datetime.date(2020,7,15), 
        start=datetime.date(2020,7,1), 
        end=datetime.date(2020,7,20)
        )

# Or you can get only the svg (str) code
svg = project.get_string_svg_for_tasks(
        today=datetime.date(2020,7,15), 
        start=datetime.date(2020,7,1), 
        end=datetime.date(2020,7,20)
)


```
* *Result*: [SVG](https://github.com/lautarodapin/gantt-lib/blob/master/file.svg?sanitize=true)




## Author

Lautaro Dapino



### Version 0.0.5
* Added `target`for the links.
* Added new method for rendering the `svg`into `str`format.

