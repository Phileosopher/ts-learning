import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'bikeSearch'
})
export class BikeSearchPipe implements PipeTransform {

  transform(items: any, searchText: string, args?: any): any {
    console.log(items);
    console.log(searchText);
    if (searchText) {
      searchText = searchText.toLowerCase();
      return items.filter((item: any) => item.model.toLowerCase().indexOf(searchText) > -1);
    }
    return items;
  }

}
