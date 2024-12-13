### About
Simple console library app where user can 
- Add and remove books with book id in json file
- Searching by 3 parametrs
	- Author
	- Year
	- Title
- Changing book status
- Display all available books 

### Example
**Before:**

```json
[
    {
        "id": "4242ad5e-daa8-46c6-9e8f-cbe543bafcb2",
        "name": "Тайна затерянного города",
        "year": 2022,
        "author": "Э.Редмонд",
        "status": "выдана"
    },
    {
        "id": "abb2e1d6-f082-42c3-9c35-725eba5cf47d",
        "name": "Зеркала времени",
        "year": 2020,
        "author": "М.Блэк",
        "status": "нет в наличии"
    },
    {
        "id": "33a304b0-d959-4cc9-9264-c441acd4061b",
        "name": "Шепот звезд",
        "year": 2021,
        "author": "И.Коста",
        "status": "в наличии"
    }
]
```
**After:**
```json
[
    {
        "id": "4242ad5e-daa8-46c6-9e8f-cbe543bafcb2",
        "name": "Тайна затерянного города",
        "year": 2022,
        "author": "Э.Редмонд",
        "status": "в наличии"
    },
    {
        "id": "abb2e1d6-f082-42c3-9c35-725eba5cf47d",
        "name": "Зеркала времени",
        "year": 2020,
        "author": "М.Блэк",
        "status": "выдана"
    },
    {
        "id": "33a304b0-d959-4cc9-9264-c441acd4061b",
        "name": "Шепот звезд",
        "year": 2021,
        "author": "И.Коста",
        "status": "нет в наличии"
    }
]
```


