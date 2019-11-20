# Custom Open edX LMS courseware search filters


## Installation

Install this package in the python environment for the LMS:

```
pip install -e git+https://github.com/open-craft/opencraft-courseware-search-filters.git@master#egg=opencraft_courseware_search_filters
```

Configure - add the following to the LMS configuration file (`lms.env.json` on
Ironwood and below; `lms.yml` on master):

```
"SEARCH_FILTER_GENERATOR": "opencraft_courseware_search_filters.ExcludeCapaSearchFilterGenerator"
```

The following filter generators are available:

- `opencraft_courseware_search_filters.ExcludeCapaSearchFilterGenerator`


## Development

TODO: add testing



## License

```
OpenCraft courseware search filters: custom courseware filters for Open edX
Copyright (C) 2019 OpenCraft

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
