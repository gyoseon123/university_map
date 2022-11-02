
// var mapOptions = {
//     center: new naver.maps.LatLng(37.3595704, 127.105399),
//     zoom: 20
// }

var map = new naver.maps.Map('map', {
    center: new naver.maps.LatLng(37.5666805, 126.9784147),
    zoom: 13,
    minZoom: 6,
    mapTypeId: naver.maps.MapTypeId.HYBRID,
    zoomControl: true,
    zoomControlOptions: {
        position: naver.maps.Position.TOP_RIGHT
    },
    mapDataControl: false,
    logoControlOptions: {
        position: naver.maps.Position.LEFT_BOTTOM
    },
    disableKineticPan: false
});
