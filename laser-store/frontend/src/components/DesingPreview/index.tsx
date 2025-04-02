import { useState, useMemo, useEffect } from 'react';
import { Canvas, useLoader } from '@react-three/fiber';
import { TextureLoader } from 'three';
import CanvasSetup from './CanvasSetup';
import MaterialControls from './MaterialControls';
import RotationHandler from './RotationHandler';
import { MATERIALS, MaterialType } from '@/config/materials';
import type { DesignPreviewProps } from './types';
import styles from './styles.module.css';

export default function DesignPreview({
  file,
  material = 'stainless-steel',
  onRotation
}: DesignPreviewProps) {
  const [rotation, setRotation] = useState<[number, number, number]>([0, 0, 0]);
  
  const materialConfig = MATERIALS[material];
  
  const [diffuseMap, normalMap] = useLoader(TextureLoader, [
    materialConfig.textureUrl || '',
    materialConfig.normalMapUrl || ''
  ]);

  const modelUrl = useMemo(() => {
    return URL.createObjectURL(file);
  }, [file]);

  useEffect(() => {
    return () => {
      // Limpiar texturas al desmontar
      if (diffuseMap) diffuseMap.dispose();
      if (normalMap) normalMap.dispose();
    };
  }, [diffuseMap, normalMap]);

  const handleRotationUpdate = (newRotation: [number, number, number]) => {
    setRotation(newRotation);
    onRotation?.(newRotation);
  };

  return (
    <div className={styles.previewContainer}>
      <MaterialControls material={material} />
      
      <Canvas camera={{ position: [0, 0, 2], fov: 45 }}>
        <CanvasSetup />
        
        <RotationHandler 
          rotation={rotation} 
          onUpdate={handleRotationUpdate}
        >
          <mesh>
            <boxGeometry args={[1, 1, 0.1]} />
            <meshStandardMaterial
              {...materialConfig}
              map={diffuseMap}
              normalMap={normalMap}
            />
          </mesh>
        </RotationHandler>
      </Canvas>
    </div>
  );
}