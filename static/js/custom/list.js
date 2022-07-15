/*
  LIST SEARCH
 */

function initListPage(url, buttonId, resultBlockId) {
    let nextUrl = url;

    $(document).ready(function () {
        nextUrl = initApiUrl + searchFilterUrl();
        $.get(nextUrl, appendNextPage);
    });

    $('.filter').change(function () {
        resultBlockId.empty()
        nextUrl = initApiUrl + searchFilterUrl();
        $.get(nextUrl, appendNextPage);
    });

    $('.search').keyup(function (e) {
        if (e.keyCode === 13) {
            e.preventDefault();
            let searchParams = new URLSearchParams(window.location.search);
            searchParams.set("search", $('#minutes').val());
            nextUrl = initApiUrl + searchFilterUrl();
            resultBlockId.empty()
            $.get(nextUrl, appendNextPage);
        }
    });

    function appendNextPage(response) {
        let countResponse = response['count'];
        nextUrl = response['next'];
        if (nextUrl === null) {
            buttonId.hide();
        }
        if (countResponse > 0) {
            response['results'].forEach(entity => {
                let card = buildCard(entity);
                resultBlockId.append(card);
            });
        } else {
            if ($('.none').length === 0) {
                resultBlockId.append(`<h4 class="none mt-2" style="color: darkgrey">There are no entries available in the selected filters</h4>`);
            }
        }
    }
}

function searchFilterUrl() {
    let queryParams = [];
    let filters = {
        'client': $('#client').val(),
        'equipment': $('#equipment').val(),
        'mode': $('#mode').val(),
        'minutes': $('#minutes').val(),
        'data_start': $('#data_start').val(),
        'data_stop': $('#data_stop').val(),
        'time_start': $('#time_start').val(),
        'time_stop': $('#time_stop').val(),

    };
    for (let key in filters) {
        if (Array.isArray(filters[key])) {
            filters[key].forEach(function (choice) {
                queryParams.push(`${key}=${choice}`)
            });
        } else {
            queryParams.push(`${key}=${filters[key]}`)
        }
    }
    return '?' + queryParams.join('&')
}


function buildCard(entity) {
    const id = entity['id'];
    const client = entity['client'];
    const equipment = entity['equipment'];
    const start = entity['start'];
    const stop = entity['stop'];
    const mode = entity['mode'];
    const minutes = entity['minutes'];

    return `
        <div class="mb-2">
            <span class="text-truncate" style="color: black">id ${id}</span>
            <span class="text-truncate" style="color: red">client ${client} </span>
            <span class="text-truncate" style="color: blue">${equipment}</span>
            <span class="text-truncate" style="color: gold">${minutes}</span>
            <span class="text-truncate" style="color: green">${start}</span>
            <span class="text-truncate" style="color: yellow">${stop}</span>
            <span class="text-truncate" style="color: purple">${mode}</span>
        </div>
`
}