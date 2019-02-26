import Vue from 'vue';
import * as moment from 'moment';

moment.locale('ja');

Vue.filter('datetimeFormat', datetimeStr => moment(datetimeStr).format('YYYY/MM/DD HH:mm'));
