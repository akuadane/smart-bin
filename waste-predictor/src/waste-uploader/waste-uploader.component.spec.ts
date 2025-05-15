import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WasteUploaderComponent } from './waste-uploader.component';

describe('WasteUploaderComponent', () => {
  let component: WasteUploaderComponent;
  let fixture: ComponentFixture<WasteUploaderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [WasteUploaderComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WasteUploaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
