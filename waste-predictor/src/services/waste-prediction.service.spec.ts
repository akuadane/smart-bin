import { TestBed } from '@angular/core/testing';

import { WastePredictionService } from './waste-prediction.service';

describe('WastePredictionService', () => {
  let service: WastePredictionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(WastePredictionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
