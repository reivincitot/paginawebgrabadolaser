import {MaterialType} from '@/config/materials.ts';

export interface DesignPreviewProps {
    file: File;
    material?: MaterialType;
    onRotation?: (rotation: [number, number, number]) => void;
    scale?: number;
    defaultRotation?: [number, number, number];
    className?: string;
}
