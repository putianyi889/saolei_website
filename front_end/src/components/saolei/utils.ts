import { MS_Level } from '@/utils/ms_const';

export enum SaoleiVideoImportState {
    NOTPLANNED = 'n',
    IMPORTING = 'i',
    IMPORTED = 'd',
    FAILED = 'f',
}

export interface SaoleiVideo {
    id: number;
    level: MS_Level;
    timems: number;
    bv: number;
    nf: boolean;
    upload_time: Date;
    import_state: SaoleiVideoImportState;
    import_video?: number;
}

export interface VideoImportEvent {
    time: Date;
    type: 'start' | 'success' | 'error' | 'getList' | 'pageEnd' | 'pageError' | 'noVideo' | 'newVideo' | 'consoleError';
    count?: number;
    video?: SaoleiVideo;
    error?: any;
}

export interface PageImportEvent {
    time: Date;
    type: 'start' | 'normal' | 'end';
    pageNumber: number;
    videoEvents: VideoImportEvent[];
}
